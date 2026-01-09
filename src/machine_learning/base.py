import pandas as pd


class PredictModel:
    POWER_655_MIN_VAL = 1
    POWER_655_MAX_VAL = 55  # assume we are using power655
    number_predict = 6
    ticket_price = 10000

    prices = {6: 40_000_000_000, 5: 5_000_000_000, 4: 500000, 3: 50000}

    col_date = "date"
    col_result = "result"
    col_predict = "predicted"
    col_predict_time = "predict_time"
    col_predict_metadata = "predict_metadata"
    col_correct = "is_correct"
    col_correct_num = "correct_num"

    def __init__(
        self,
        df: pd.DataFrame,
        time_predict: int = 1,
        min_val: int = POWER_655_MIN_VAL,
        max_val: int = POWER_655_MAX_VAL,
    ):
        self.df = df
        self.df_backtest = None
        self.df_backtest_explode = None
        self.df_backtest_evaluate = None
        self.time_predict = time_predict
        self.min_val = min_val
        self.max_val = max_val

    @classmethod
    def _count_number(cls, number_series):
        return number_series.explode().value_counts().to_frame("times")

    @classmethod
    def _compare_list(cls, l1, l2):
        l1_s = set(l1)
        l2_s = set(l2)
        inter = l1_s.intersection(l2_s)
        return len(inter) == len(l1), len(inter)

    def predict(self, date):
        pass

    def backtest(self):
        _df = self.df.copy()

        def fn_apply(row):
            predicted = []
            for i in range(self.time_predict):
                loop_predict = self.predict(row.date)
                correct, correct_num = self._compare_list(row.result, loop_predict)
                predicted.append(
                    {
                        PredictModel.col_predict + "_idx": i,
                        PredictModel.col_predict: loop_predict,
                        PredictModel.col_correct: correct,
                        PredictModel.col_correct_num: correct_num,
                    }
                )

            return predicted

        _df["predict_metadata"] = _df.apply(fn_apply, axis=1)
        self.df_backtest = _df

    def evaluate(self):
        self.df_backtest_explode = self.df_backtest.explode(PredictModel.col_predict_metadata)
        self.df_backtest_evaluate = pd.concat(
            [
                self.df_backtest_explode.reset_index(drop=True),
                pd.json_normalize(self.df_backtest_explode[PredictModel.col_predict_metadata]),
            ],
            axis="columns",
        )

        return {
            "correct_time": self.df_backtest_evaluate[PredictModel.col_correct].sum(),
            "count_correct_num": self.df_backtest_evaluate.value_counts(PredictModel.col_correct_num),
        }

    def get_distribution_stats(self):
        """Analyze the probability distribution of drawn numbers."""
        all_results = self.df[self.col_result].explode()
        stats = all_results.value_counts().sort_index()
        total_draws = len(self.df)
        
        # Expected frequency if perfectly random (Uniform distribution)
        expected_freq = (total_draws * self.number_predict) / (self.max_val - self.min_val + 1)
        
        df_stats = pd.DataFrame({
            "number": stats.index,
            "actual_freq": stats.values,
            "expected_freq": expected_freq,
            "deviation": stats.values - expected_freq,
            "relative_freq": stats.values / (total_draws * self.number_predict)
        })
        return df_stats

    def revenue(self):
        cost = len(self.df_backtest_evaluate) * self.ticket_price
        gain = self.df_backtest_evaluate[PredictModel.col_correct_num].map(self.prices).fillna(0).astype(int).sum()

        return cost, gain, gain - cost

    def run_monte_carlo(self, n_simulations=1000, n_draws=100):
        """
        Run Monte Carlo simulations to evaluate the risk-weighted outcomes.
        """
        import numpy as np
        import random
        
        profits = []
        for _ in range(n_simulations):
            sim_profit = 0
            for _ in range(n_draws):
                daily_cost = self.time_predict * self.ticket_price
                sim_profit -= daily_cost
                
                draw = random.sample(range(self.min_val, self.max_val + 1), self.number_predict)
                predictions = [self.predict(None) for _ in range(self.time_predict)]
                
                for pred in predictions:
                    _, num_correct = self._compare_list(draw, pred)
                    if num_correct in self.prices:
                        sim_profit += self.prices[num_correct]
            
            profits.append(sim_profit)
            
        profits = np.array(profits)
        return {
            "mean_profit": float(profits.mean()),
            "std_profit": float(profits.std()),
            "prob_of_profit": float((profits > 0).mean()),
            "max_profit": float(profits.max()),
            "min_profit": float(profits.min())
        }
