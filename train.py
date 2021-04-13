# coding: utf-8
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import joblib


X, y = load_iris(return_X_y=True)
dtc = DecisionTreeClassifier()
dtc.fit(X, y)

joblib.dump(dtc, 'models/decision_tree.joblib')
