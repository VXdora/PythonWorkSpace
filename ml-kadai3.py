from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

wine = datasets.load_wine()
x = wine.data
y = wine.target

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3)

from sklearn.svm import SVC
model = SVC(kernel='linear')
model.fit(xtrain, ytrain)

ans = model.predict(xtest)
print(sum(ans == ytest) / len(ytest))
