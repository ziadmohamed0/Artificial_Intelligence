######################################
# @file   : 08_Confusion_Matrix.py   #
# @brief  : Confusion_Matrix session #
# @auther : Ziad Mohammed Fathi      #
######################################

import numpy as np
import seaborn as sns
import sklearn.ensemble as skle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score , f1_score ,accuracy_score , recall_score, confusion_matrix
from sklearn.datasets import load_digits

x, y = load_digits(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)

clf = skle.RandomForestClassifier(random_state=23)
clf.fit(x_train, y_train)

y_predic = clf.predict(x_test)
cm = confusion_matrix(y_test, y_predic)

sns.heatmap(cm,annot=True,fmt='g')
plt.ylabel('Prediction')
plt.xlabel('Acual')
plt.title('Counfusion Matrix')

plt.show()
