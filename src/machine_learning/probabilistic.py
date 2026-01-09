import numpy as np
import pandas as pd
from typing import List, Dict, Any, Tuple
from datetime import date
import random
from machine_learning.base import PredictModel
from loguru import logger

class BayesianInferenceStrategy(PredictModel):
    """
    Strategy that uses Bayesian updating to estimate the probability of each number.
    It treats the lottery as a Dirichlet-Multinomial process (though it's technically 
    sampling without replacement, this is a common approximation).
    """

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = PredictModel.POWER_655_MIN_VAL,
        max_val: int = PredictModel.POWER_655_MAX_VAL,
        prior_strength: float = 1.0, # Alpha for Dirichlet prior
    ):
        super().__init__(df, time_predict, min_val, max_val)
        self.prior_strength = prior_strength
        self.num_possible = max_val - min_val + 1

    def _get_number_counts(self, target_date: date) -> pd.Series:
        mask = (self.df["date"] < target_date)
        history = self.df[mask]["result"].explode().value_counts()
        
        # Ensure all numbers are represented
        all_nums = pd.Series(0, index=range(self.min_val, self.max_val + 1))
        return history.add(all_nums, fill_value=0).sort_index()

    def predict(self, target_date: date) -> List[int]:
        if target_date is None or pd.isna(target_date):
            # Fallback to random if no date provided or invalid date
            all_numbers = list(range(self.min_val, self.max_val + 1))
            return sorted(random.sample(all_numbers, self.number_predict))

        counts = self._get_number_counts(target_date)
        
        # Bayesian Posterior (Dirichlet-Multinomial)
        # We add prior_strength to each count
        posterior_probs = (counts + self.prior_strength) / (counts.sum() + self.num_possible * self.prior_strength)
        
        # Sampling based on posterior probabilities
        predicted = []
        available_nums = list(range(self.min_val, self.max_val + 1))
        probs = posterior_probs.values.tolist()
        
        # Sample 6 numbers without replacement
        while len(predicted) < self.number_predict:
            # Normalize probs to ensure sum is 1.0
            p_sum = sum(probs)
            p_norm = [p/p_sum for p in probs]
            
            chosen = np.random.choice(available_nums, p=p_norm)
            idx = available_nums.index(chosen)
            
            predicted.append(int(chosen))
            
            # Remove chosen to sample without replacement
            available_nums.pop(idx)
            probs.pop(idx)
            
        return sorted(predicted)

class PoissonGapStrategy(PredictModel):
    """
    Strategy based on the 'Wait' time (gap) between draws for each number.
    According to Poisson process, the time between events follows Exponential distribution.
    Numbers 'overdue' compared to their average gap are weighted higher.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = PredictModel.POWER_655_MIN_VAL,
        max_val: int = PredictModel.POWER_655_MAX_VAL,
    ):
        super().__init__(df, time_predict, min_val, max_val)

    def _analyze_gaps(self, target_date: date) -> Dict[int, float]:
        mask = (self.df["date"] < target_date)
        history = self.df[mask].sort_values("date")
        
        last_drawn = {i: -1 for i in range(self.min_val, self.max_val + 1)}
        gaps = {i: [] for i in range(self.min_val, self.max_val + 1)}
        
        for idx, row in history.iterrows():
            current_draw_idx = idx
            for num in row["result"]:
                if num in last_drawn and last_drawn[num] != -1:
                    gaps[num].append(current_draw_idx - last_drawn[num])
                last_drawn[num] = current_draw_idx

        # Calculate "Overdue" score
        current_idx = len(history)
        scores = {}
        for num in range(self.min_val, self.max_val + 1):
            avg_gap = np.mean(gaps[num]) if gaps[num] else 30 # Default if no data
            current_gap = current_idx - last_drawn[num] if last_drawn[num] != -1 else 50
            
            # Using Exponential survival function: P(X > t) = exp(-lambda * t)
            # lambda = 1 / avg_gap
            # Score is higher if current_gap is larger than avg_gap
            overdue_ratio = current_gap / avg_gap
            scores[num] = overdue_ratio

        return scores

    def predict(self, target_date: date) -> List[int]:
        if target_date is None or pd.isna(target_date):
            # Fallback to random if no date provided or invalid date
            all_numbers = list(range(self.min_val, self.max_val + 1))
            return sorted(random.sample(all_numbers, self.number_predict))

        scores = self._analyze_gaps(target_date)
        
        # Sort by overdue score descending
        sorted_nums = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        
        # Take top candidates and sample for variety
        top_picks = [int(n[0]) for n in sorted_nums[:15]]
        
        return sorted(random.sample(top_picks, self.number_predict))
