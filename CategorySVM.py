from sklearn import svm
from sklearn.model_selection import train_test_split

# TODO: lmao all of it still, I've been using https://www.datacamp.com/tutorial/svm-classification-scikit-learn-python
#       but like, whatever works.

class CategoryClassifer:
    def __init__(self, data, answers):
        self.X_train, self.X_test, self.Y_train, self.Y_test =\
            train_test_split(data, answers,
                             test_size=0.2, random_state=5)
