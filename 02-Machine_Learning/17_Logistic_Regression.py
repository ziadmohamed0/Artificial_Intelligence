#########################################
# @file   : 17_Logistic_Regression.py   #
# @brief  : Logistic Regression session #
# @auther : Ziad Mohammed Fathi         #
#########################################


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report
from sklearn.datasets import make_classification

x, y = make_classification(n_samples=1000, n_features=2 , n_informative=2 , n_redundant=0, n_clusters_per_class=1 ,random_state=42)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression(random_state=42)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy: ",accuracy_score(y_test, y_pred))
print("\nConfusion Matrix : ")
print(confusion_matrix(y_test, y_pred))
print("\nClassification report : ")
print(classification_report(y_test, y_pred))