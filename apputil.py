import pandas as pd


class GroupEstimate(object):
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

        column_names = self.group_estimates.index.names
        # Gathering the names of the columns from our estimates

        if isinstance(X, pd.DataFrame):
            X_New = X_[column_names]
        elif len(column_names) == 1:
            X_New = pd.DataFrame({column_names[0]: X_})
        else:
            X_New = pd.DataFrame(X_, columns=column_names)
        # Creating X_New based on estimates and column names.

        if isinstance(self.group_estimates.index, pd.MultiIndex):
            groups = pd.MultiIndex.from_frame(X_New)
        else:
            groups = X_New.iloc[:, 0]
        # Finding groups of estimates.

        predictions = self.group_estimates.reindex(groups)

        missing = predictions.isna().sum()

        if missing > 0:
            print(
                f"{missing} groups were not in the training data. Filling with NaN.")

        return predictions.to_numpy()
