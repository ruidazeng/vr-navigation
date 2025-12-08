"""
K-means clustering on (posX, posZ) tuples for a single subject.
"""
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

# Configuration
DATA_DIR = 'Parsed Data'
filename = 'AAAA.csv'
k = 8  # Number of clusters

# Read data
data = pd.read_csv(os.path.join(DATA_DIR, filename))
print('data:', data.shape)

# Getting the values
x = data['posX'].values
y = data['posZ'].values

# X is the dataset
X = np.array(list(zip(x, y)))

# Plotting original data
plt.scatter(x, y, c='olive', s=20)
plt.xlabel("X axis")
plt.ylabel("Z axis")
plt.title("Coordinates in the Learning Maze")

# K-Means clustering
kmeans = KMeans(n_clusters=k, n_init='auto')
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

print(y_kmeans)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='plasma')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

plt.show()
