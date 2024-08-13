######################################
# @file   : 16_Cross_Validation.py   #
# @brief  : Cross Validation session #
# @auther : Ziad Mohammed Fathi      #
######################################

from sklearn.datasets import load_iris
from sklearn.model_selection import KFold, cross_val_score
from sklearn.svm import SVC

iris = load_iris()
x,y = iris.data , iris.target

svm_classifier= SVC(kernel='linear', C=1)
kfold = KFold(n_splits=5 , shuffle=True , random_state=42)
accuracy_sources = cross_val_score(svm_classifier , x , y , cv=kfold)

print("Accuracy Sorce for each fold: ", accuracy_sources)
print("Mean Accuracy : ", accuracy_sources.mean())