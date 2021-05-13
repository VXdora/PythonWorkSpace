import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_covtype

covdata = fetch_covtype()

x = covdata.data
y = covdata.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

clf = LDA()
clf.fit(x_train, y_train)
sc = clf.score(x_test, y_test)
print(sc)
