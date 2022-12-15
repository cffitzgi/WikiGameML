from sklearn.linear_model import LogisticRegression

# Source: https://machinelearningmastery.com/multinomial-logistic-regression-with-python/

class Heuristic:
    def __init__(self, dataset):
        self.model = LogisticRegression(multi_class="multinomial", solver="lbfgs")



