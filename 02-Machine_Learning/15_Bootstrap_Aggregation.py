###########################################
# @file   : 15_Bootstrap_Aggregation.py   #
# @brief  : Bootstrap Aggregation session #
# @auther : Ziad Mohammed Fathi           #
###########################################

import numpy as np
import pandas as pa
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import load_digits

digits = load_digits()
x,y = digits.data , digits.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


base_classifier = DecisionTreeClassifier(random_state=42)
bagging_classifier = BaggingClassifier(base_classifier, n_estimators=10 , random_state=42)

bagging_classifier.fit(x_train, y_train)
y_pred = bagging_classifier.predict(x_test)

print("Accuracy : ", accuracy_score(y_test,y_pred))