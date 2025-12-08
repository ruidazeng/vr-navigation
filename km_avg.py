"""
3D representation of the average (mean) position of clusters over time.
Time is the Z-axis. Shows averaged paths for each cluster.
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

# Decimation factor for visualization
DECIMATE = 10
NUM_POINTS = 30000 // DECIMATE  # Expected number of decimated points

# Plot 3D averaged paths by clusters
for item in sorted(clusters):
    print("Cluster", item)
    
    # Create the plot window
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Accumulate positions for averaging
    X_sum = np.zeros(NUM_POINTS)
    Y_sum = np.zeros(NUM_POINTS)
    file_count = 0
    
    for filename in clusters[item]:
        data = pd.read_csv(os.path.join(SUBDIRECT, filename))
        small_x = data['posX'].values[::DECIMATE]
        small_y = data['posZ'].values[::DECIMATE]
        
        # Only include files with expected number of points
        if len(small_x) >= NUM_POINTS and len(small_y) >= NUM_POINTS:
            X_sum[:NUM_POINTS] += small_x[:NUM_POINTS]
            Y_sum[:NUM_POINTS] += small_y[:NUM_POINTS]
            file_count += 1
    
    # Calculate averages (avoid division by zero)
    if file_count > 0:
        X_avg = X_sum / file_count
        Y_avg = Y_sum / file_count
    else:
        print(f"  Warning: No valid files in cluster {item}")
        plt.close(fig)
        continue
    
    t_size = len(X_avg)
    # Color gradient (red=early, blue=late)
    colorGrad = [[j / t_size, 0, 1 - j / t_size] for j in range(t_size)]
    time = list(range(t_size))
    
    ax.scatter(X_avg, Y_avg, time, c=colorGrad)
    ax.set_xlabel('posX (avg)')
    ax.set_ylabel('posZ (avg)')
    ax.set_zlabel('Time')
    plt.title(f'Cluster {item} - Average Path ({file_count} subjects)')
    plt.show()
