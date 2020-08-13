import numpy as np
from sklearn import preprocessing, neighbors
from sklearn.model_selection import train_test_split
import pandas as pd


class KNNClassifier:
    def __init__(self, dataset_path, label_name):
        self.dataset_path = dataset_path
        self.df = pd.read_csv(dataset_path)
        self.label = label_name

    def Train(self):
        self.preprocessData()
        X = np.array(self.df.drop(['worthy'], 1))
        Y = np.array(self.df['worthy'])
        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, test_size=0.2)

        clf = neighbors.KNeighborsClassifier(n_neighbors=2)
        clf.fit(X_train, Y_train)
        return clf

    def preprocessData(self):
        self.df['price'] = self.df['price'] / 100
        print(self.df.head())
