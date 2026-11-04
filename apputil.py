import pandas as pd


def GroupEstimate(object):
    def __init__(self, estimate):
        if estimate not in ['mean', 'median']:
            raise ValueError(
                "Estimate is not 'mean' or 'median', please choose one.")
        # Adding an estimate variable for mean or median.

        self.estimate = estimate

    def fit(self, X, y):
        if len(X) != len(y):
            raise ValueError("X and y do not have the same length.")
            # Installing a check so that our X and y are the same length

        df = pd.concat([X, pd.Series(y, name='target')], axis=1)
        # Combing our same length X and y into a df named df.

        grouped = df.groupby(list(X.columns))
        # Grouping our df

        # Make our actual mean and median estimates, mean is first cause idk.
        if self.estimate == 'mean':
            self.group_estimates = grouped['target'].mean()
        else:
            self.group_estimates = grouped['target'].median()

        return self

    def predict(self, X):
        return None
