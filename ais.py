import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class AISClassifier:
    def __init__(self, n_antibodies= 10):
        self.n = n_antibodies
        self.antibodies = None
        self.labels = None

    def fit(self, x, y):
        idx = np.random.choice(len(x), self.n, replace=False)
        self.antibodies = x[idx]
        self.labels = y[idx]

    def predict(self, x):
        return [
            self.labels[np.argmin(np.linalg.norm(self.antibodies-x,axis=1))]
            for x in x
        ]
    
x,y = load_iris(return_X_y=True)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

result = AISClassifier(10)
result.fit(x_train,y_train)
y_pred = result.predict(x_test)
print(accuracy_score(y_pred,y_test))
