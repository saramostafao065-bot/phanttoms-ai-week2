from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
import numpy as np

d = load_iris()
x, y = d.data, d.target

splitter = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

model1 = DecisionTreeClassifier(random_state=42)
model2 = LogisticRegression(max_iter=1000)

s1 = cross_val_score(model1, x, y, cv=splitter)
s2 = cross_val_score(model2, x, y, cv=splitter)

print(np.mean(s1), np.std(s1))
print(np.mean(s2), np.std(s2))
