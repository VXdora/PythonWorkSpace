from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = load_wine()
x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.5)
model = RandomForestClassifier()
model.fit(x_train, y_train)
ans = model.predict(x_test)
pre = (ans == y_test).sum() / len(ans)
print('RandomForest:', pre)

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(x_train, y_train)
ans = model.predict(x_test)
pre = (ans == y_test).sum() / len(ans)
print('Native Bayes:', pre)
