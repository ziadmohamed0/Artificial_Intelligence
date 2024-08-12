###################################
# @file   : 07_Decision_Tree.py   #
# @brief  : Decision Tree session #
# @auther : Ziad Mohammed Fathi   #
###################################

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

iris = load_iris()
x, y = iris.data, iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(x_train, y_train)
y_predict = clf.predict(x_test)

accuracy = accuracy_score(y_test, y_predict)
print("Accuracy : ", accuracy)