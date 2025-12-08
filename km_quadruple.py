"""
K-means clustering based on time spent at 4 decision points (intersections).
Calculates quadruples representing normalized time at each intersection.
"""
import os
import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def calculate_distance(x1, y1, x2, y2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def find_quadruple(subdirect, filename):
    """
    Calculate time spent near each of 4 decision points.
    Returns normalized quadruple [time_at_1, time_at_2, time_at_3, time_at_4].
    """
    quadruple = [0, 0, 0, 0]
    data = pd.read_csv(os.path.join(subdirect, filename))
    X = data['posX'].values
    Y = data['posZ'].values
    
    # Decision point coordinates in the maze
    decision_points = [
        (-2.5, 2.1),   # Intersection 1
        (-1.1, -2.0),  # Intersection 2
        (1.5, -2.5),   # Intersection 3
        (1.9, 1.35)    # Intersection 4
    ]
    
    epsilon = 0.8  # Proximity threshold
    
    for x, y in zip(X, Y):
        for i, (px, py) in enumerate(decision_points):
            dist = calculate_distance(x, y, px, py)
            if dist <= epsilon:
                quadruple[i] += 1
    
    # Normalize by total data points
    for i in range(4):
        quadruple[i] /= 30000
        quadruple[i] = round(quadruple[i], 3)
    
    return quadruple


rootdir = os.getcwd()
arr = []
row_dict = []  # Store filenames for cluster membership

# Process all CSV files
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if '.csv' in file:
            qua = find_quadruple(subdir, file)
            arr.append(qua)
            row_dict.append(file)

X = np.array(arr)

# Number of clusters
k = 4

# K-Means clustering
kmeans = KMeans(n_clusters=k, n_init='auto')
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Build clusters dictionary
clusters = {}
for n, item in enumerate(y_kmeans):
    if item in clusters:
        clusters[item].append(row_dict[n])
    else:
        clusters[item] = [row_dict[n]]

for item in sorted(clusters):
    print("Cluster", item)
    for filename in clusters[item]:
        print(filename)

# 2D Projection presentations
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
plt.xlabel('Decision Point 1')
plt.ylabel('Decision Point 2')
plt.title('Cluster Projection (DP1 vs DP2)')
plt.show()

plt.scatter(X[:, 1], X[:, 2], c=y_kmeans, s=50, cmap='viridis')
plt.xlabel('Decision Point 2')
plt.ylabel('Decision Point 3')
plt.title('Cluster Projection (DP2 vs DP3)')
plt.show()

plt.scatter(X[:, 2], X[:, 3], c=y_kmeans, s=50, cmap='viridis')
plt.xlabel('Decision Point 3')
plt.ylabel('Decision Point 4')
plt.title('Cluster Projection (DP3 vs DP4)')
plt.show()

plt.scatter(X[:, 0], X[:, 2], c=y_kmeans, s=50, cmap='viridis')
plt.xlabel('Decision Point 1')
plt.ylabel('Decision Point 3')
plt.title('Cluster Projection (DP1 vs DP3)')
plt.show()

plt.scatter(X[:, 0], X[:, 3], c=y_kmeans, s=50, cmap='viridis')
plt.xlabel('Decision Point 1')
plt.ylabel('Decision Point 4')
plt.title('Cluster Projection (DP1 vs DP4)')
plt.show()

plt.scatter(X[:, 1], X[:, 3], c=y_kmeans, s=50, cmap='viridis')
plt.xlabel('Decision Point 2')
plt.ylabel('Decision Point 4')
plt.title('Cluster Projection (DP2 vs DP4)')
plt.show()

# 3D Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=y_kmeans, s=50, cmap='viridis')
ax.set_xlabel('Decision Point 1')
ax.set_ylabel('Decision Point 2')
ax.set_zlabel('Decision Point 3')
plt.title('3D Cluster View (DP1, DP2, DP3)')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 1], X[:, 2], X[:, 3], c=y_kmeans, s=50, cmap='viridis')
ax.set_xlabel('Decision Point 2')
ax.set_ylabel('Decision Point 3')
ax.set_zlabel('Decision Point 4')
plt.title('3D Cluster View (DP2, DP3, DP4)')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 2], X[:, 3], c=y_kmeans, s=50, cmap='viridis')
ax.set_xlabel('Decision Point 1')
ax.set_ylabel('Decision Point 3')
ax.set_zlabel('Decision Point 4')
plt.title('3D Cluster View (DP1, DP3, DP4)')
plt.show()
