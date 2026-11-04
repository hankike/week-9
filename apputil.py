import pandas as pd


def GroupEstimate(object):
    def __init__(self, estimate):
        if estimate not in ['mean', 'median']:
            raise ValueError(
                "Estimate is not 'mean' or 'median', please choose one.")
        # Adding an estimate variable for mean or median.

        self.estimate = estimate

    def fit(self, X, y):
        return None

    def predict(self, X):
        return None
