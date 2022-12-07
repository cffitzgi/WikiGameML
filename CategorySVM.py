from sklearn import svm
from sklearn.model_selection import train_test_split

class CategoryClassifer:
    def __init__(self, data, answers):
        self.X_train, self.X_test, self.Y_train, self.Y_test =\
            train_test_split(data, answers,
                             test_size=0.2, random_state=5)
