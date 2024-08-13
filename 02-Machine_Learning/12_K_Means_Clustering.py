########################################
# @file   : 12_K_Means_Clustering.py   #
# @brief  : K Means Clustering session #
# @auther : Ziad Mohammed Fathi        #
########################################

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

x,y = make_blobs(n_samples=300, centers=3, random_state=42)
Kmeans_modul = KMeans(n_clusters=3 , random_state=42)

Kmeans_modul.fit(x)
cluster_centers = Kmeans_modul.cluster_centers_
lables = Kmeans_modul.labels_

plt.scatter(x[:, 0], x[:, 1],c=lables,cmap='viridis', edgecolors='k',s=50)
plt.scatter(cluster_centers[: , 0],cluster_centers[: , 1],c='red',marker='X', s=200)
plt.xlabel('figure 1')
plt.ylabel('figure 2')
plt.legend()
plt.show()
