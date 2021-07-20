from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
X = iris.data.astype(np.float32)
U, S, Vt = np.linalg.svd(X)

Vt2 = Vt[0:2, :]
X2 = np.dot(X, Vt2.T)
print(kiyo(X2))

Vt3 = Vt[0:3, :]
X3 = np.dot(X, Vt3.T)
print(kiyo(X3))

