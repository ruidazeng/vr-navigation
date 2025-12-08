"""
K-means clustering on decimated position vectors with temporal color coding.
Red indicates early, blue indicates late.
"""
import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def find_vector(subdirect, filename):
    """Create a feature vector from decimated X and Z positions."""
    vec = []
    data = pd.read_csv(os.path.join(subdirect, filename))
    X = data['posX'].values[0:30000:1000]
    Y = data['posZ'].values[0:30000:1000]
    
    if len(X) != 30 or len(Y) != 30:
        return vec  # Return empty list if data doesn't match expected size
    
    for x in X:
        vec.append(x)
    for y in Y:
        vec.append(y)
    return vec


rootdir = os.getcwd()
arr = []
row_dict = []  # Store filenames for cluster membership
SUBDIRECT = None

# Process all CSV files
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if '.csv' in file:
            if not SUBDIRECT:
                SUBDIRECT = subdir
            
            tmp = find_vector(subdir, file)
            if not tmp:
                print('Invalid file (for this decimation strategy):', file)
                continue
            arr.append(tmp)
            row_dict.append(file)

X = np.array(arr)

# Number of clusters
k = 8

# K-Means clustering
kmeans = KMeans(n_clusters=k, n_init='auto')
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
print(y_kmeans)

# Build clusters dictionary
clusters = {}
for n, item in enumerate(y_kmeans):
    if item in clusters:
        clusters[item].append(row_dict[n])
    else:
        clusters[item] = [row_dict[n]]

for item in sorted(clusters):
    print("Cluster", item)
    print(clusters[item])

# Color gradient (red=early, blue=late)
colorGrad = [[i / 30, 0, 1 - i / 30] for i in range(30)]

# Plot points by clusters
for item in sorted(clusters):
    print("Cluster", item)
    for filename in clusters[item]:
        data = pd.read_csv(os.path.join(SUBDIRECT, filename))
        X = data['posX'].values[0:30000:1000]
        Y = data['posZ'].values[0:30000:1000]
        plt.scatter(X, Y, c=colorGrad)
    plt.title(f'Cluster {item}')
    plt.xlabel('posX')
    plt.ylabel('posZ')
    plt.show()
