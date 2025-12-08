"""
Failed attempt at k-means clustering all (posX, posZ) in tuple forms.
Returns ValueError: Found array with dim 3. Estimator expected <= 2.

This script demonstrates a problematic approach that doesn't work,
kept for educational/historical purposes.
"""
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

# Configuration
DATA_DIR = 'Parsed Data'

# Read data files
data1 = pd.read_csv(os.path.join(DATA_DIR, 'AAAA.csv'))
print('data1:', data1.shape)

data2 = pd.read_csv(os.path.join(DATA_DIR, 'ACGN.csv'))
print('data2:', data2.shape)

data3 = pd.read_csv(os.path.join(DATA_DIR, 'AELV.csv'))
print('data3:', data3.shape)

data4 = pd.read_csv(os.path.join(DATA_DIR, 'ANAV.csv'))
print('data4:', data4.shape)

data5 = pd.read_csv(os.path.join(DATA_DIR, 'AOXY.csv'))
print('data5:', data5.shape)

# Getting the values
x1 = data1['posX'].values
y1 = data1['posZ'].values

x2 = data2['posX'].values
y2 = data2['posZ'].values

x3 = data3['posX'].values
y3 = data3['posZ'].values

x4 = data4['posX'].values
y4 = data4['posZ'].values

x5 = data5['posX'].values
y5 = data5['posZ'].values

# X is the dataset - THIS CREATES A 3D ARRAY WHICH CAUSES THE ERROR
X = np.array(list(zip(zip(x1, y1), zip(x2, y2), zip(x3, y3), zip(x4, y4), zip(x5, y5))))

# Number of clusters
k = 2

kmeans = KMeans(n_clusters=k, n_init='auto')
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

print(y_kmeans)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

plt.show()
