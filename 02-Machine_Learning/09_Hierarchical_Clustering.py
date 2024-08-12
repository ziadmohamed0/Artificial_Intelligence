#############################################
# @file   : 09_Hierarchical_Clustering.py   #
# @brief  : Hierarchical Clustering session #
# @auther : Ziad Mohammed Fathi             #
#############################################

import numpy as np
import seaborn as sns
import sklearn.ensemble as skle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score , f1_score ,accuracy_score , recall_score, confusion_matrix
from sklearn.datasets import load_digits, make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

x,y = make_blobs(n_samples=300, centers=4, random_state=42)
linkage_matrix = linkage(x, method='ward')

plt.figure(figsize=(10,5))
dendrogram(linkage_matrix)

plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()

clusters = AgglomerativeClustering(n_clusters=4, linkage='ward')
y_predic = clusters.fit_predict(x)

plt.scatter(x[:,0], x[:,1], c=y_predic , cmap='viridis')
plt.title('Agglomerative Hierarchical Clustering')
plt.show()