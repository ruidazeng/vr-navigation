"""
3D visualization of k-means clusters with time as Z-axis.
Red indicates early positions, blue indicates late positions.
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

# Plot 3D visualization by clusters
for item in sorted(clusters):
    print("Cluster", item)
    
    # Create the plot window
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for filename in clusters[item]:
        data = pd.read_csv(os.path.join(SUBDIRECT, filename))
        X_pos = data['posX'].values[::100]
        Y_pos = data['posZ'].values[::100]
        
        t_size = len(X_pos)
        # Color gradient (red=early, blue=late)
        colorGrad = [[j / t_size, 0, 1 - j / t_size] for j in range(t_size)]
        time = list(range(t_size))
        
        ax.scatter(X_pos, Y_pos, time, c=colorGrad)
    
    ax.set_xlabel('posX')
    ax.set_ylabel('posZ')
    ax.set_zlabel('Time')
    plt.title(f'Cluster {item} - 3D View')
    plt.show()
