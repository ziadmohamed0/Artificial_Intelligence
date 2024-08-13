#################################
# @file   : 10_Grid_Search.py   #
# @brief  : Grid Search session #
# @auther : Ziad Mohammed Fathi #
#################################

from sklearn import datasets
from sklearn.model_selection import train_test_split , GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

iris = datasets.load_iris()
x,y = iris.data , iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

param_grid1 = {'c': [0.1,1,10,100], 'gamma': [0.01,0.1,1,10], 'kernel': ['linear', 'rbf', 'poly']}
svm_classifier1 = SVC()

grid_search = GridSearchCV(svm_classifier1, param_grid1 ,cv=5, scoring='accuracy')
grid_search.fit(x_train, y_train)

best_params = grid_search.best_params_
best_modul = grid_search.best_estimator_

y_pred = best_modul.predict(x_test)

print("Best Parameter       : ", best_params)
print("Accuracy on test set : ", accuracy_score(y_test,y_pred))
