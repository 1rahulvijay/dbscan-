# DBSCAN Clustering

# Importing the libraries
import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values


# Using the elbow method to find the optimal number of clusters
from sklearn.cluster import DBSCAN
dbscan=DBSCAN(eps=5,min_samples=5)

# Fitting the model

model=dbscan.fit(X)

labels=model.labels_


from sklearn import metrics

#identifying the points which makes up our core points
sample_cores=np.zeros_like(labels,dtype=bool)
print(sample_cores)

sample_core = sample_cores[dbscan.core_sample_indices_]=True
print(sample_core)

#Calculating the number of clusters

n_clusters=len(set(labels))- (1 if -1 in labels else 0)
print((n_clusters))



print(metrics.silhouette_score(X,labels))



