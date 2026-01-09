import numpy as np
import pandas as pd
from typing import List, Dict, Any, Type
import random
from machine_learning.base import PredictModel
from loguru import logger

class MonteCarloSimulator:
    """
    Monte Carlo Simulator for lottery strategies.
    Simulates thousands of games to determine the statistical significance of a strategy.
    """

    def __init__(
        self,
        strategy_class: Type[PredictModel],
        df_history: pd.DataFrame,
        num_simulations: int = 1000,
        iterations_per_sim: int = 100,
        **strategy_params
    ):
        self.strategy_class = strategy_class
        self.df_history = df_history
        self.num_simulations = num_simulations
        self.iterations_per_sim = iterations_per_sim
        self.strategy_params = strategy_params

    def run_simulation(self) -> Dict[str, Any]:
        """
        Runs the Monte Carlo simulation.
        
        Returns:
            Dictionary containing simulation statistics.
        """
        logger.info(f"Starting Monte Carlo simulation: {self.num_simulations} runs")
        results = []

        for i in range(self.num_simulations):
            # Create strategy instance
            strategy = self.strategy_class(self.df_history, **self.strategy_params)
            
            # Simulate a single run (multiple draws)
            hits = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
            for _ in range(self.iterations_per_sim):
                theoretical_draw = random.sample(
                    range(strategy.min_val, strategy.max_val + 1), 
                    strategy.number_predict
                )
                
                prediction = strategy.predict(pd.Timestamp.now().date())
                
                _, num_correct = strategy._compare_list(theoretical_draw, prediction)
                hits[num_correct] += 1
            
            results.append(hits)

        # Aggregate results
        df_results = pd.DataFrame(results)
        summary = {
            "mean_hits": df_results.mean().to_dict(),
            "max_hits": df_results.max().to_dict(),
            "win_probability_3plus": (df_results[[3, 4, 5, 6]].sum(axis=1) > 0).mean()
        }
        
        return summary
                
                # Predict
                prediction = strategy.predict(pd.Timestamp.now().date())
                
                # Check matches
                _, matches = strategy._compare_list(theoretical_draw, prediction)
                
                # Calculate profit
                current_net_profit += strategy.prices.get(matches, 0) - strategy.ticket_price
            
            results.append(current_net_profit)

        results_series = pd.Series(results)
        
        summary = {
            "mean_profit": results_series.mean(),
            "std_profit": results_series.std(),
            "min_profit": results_series.min(),
            "max_profit": results_series.max(),
            "median_profit": results_series.median(),
            "prob_of_loss": (results_series < 0).mean(),
            "confidence_interval_95": (
                results_series.quantile(0.025),
                results_series.quantile(0.975)
            )
        }
        
        return summary

    def simulate_data(self, n_rows: int = 1000) -> pd.DataFrame:
        """
        Simulate a synthetic lottery dataset based on current history statistics.
        """
        all_nums = self.df_history['result'].explode().dropna().values
        # Simple bootstrap resampling
        simulated_results = []
        for _ in range(n_rows):
            res = np.random.choice(all_nums, size=6, replace=False).tolist()
            simulated_results.append(res)
            
        df_sim = pd.DataFrame({
            'date': pd.date_range(start='2026-01-01', periods=n_rows),
            'id': [f"SIM_{i:05d}" for i in range(n_rows)],
            'result': simulated_results
        })
        return df_sim
