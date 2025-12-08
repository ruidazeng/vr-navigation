# Clustering Scripts

K-means clustering algorithms for analyzing subject navigation patterns in VR maze data.

## Scripts

### Single Subject Analysis

#### `km_linear.py`
Basic k-means clustering on (posX, posZ) position tuples for a single subject. Clusters spatial positions in the maze.

![k-means linear plot](/Resources/km_linear.png)

### Multi-Subject Analysis

#### `km_quadruple.py`
Clusters subjects based on **time spent at 4 decision points** (maze intersections). Creates a 4-dimensional feature vector representing hesitation time at each intersection.

Decision point coordinates:
- Intersection 1: (-2.5, 2.1)
- Intersection 2: (-1.1, -2.0)
- Intersection 3: (1.5, -2.5)
- Intersection 4: (1.9, 1.35)

![k-means quadruple plot](/Resources/km_quadruple.png)

#### `km_vector.py`
Creates 60-element feature vectors (30 decimated X + 30 Z positions) per subject, then clusters subjects by navigation similarity. Excludes 2 files due to decimation requirements.

![k-means vector plot](/Resources/km_vector.png)

#### `km_vector_more.py`
Same as above but with finer decimation (every 10th point). Creates 6000-element vectors. Excludes 39 files due to stricter requirements.

![k-means vector more plot](/Resources/km_vector_more.png)

### Temporal Visualizations

#### `km_color.py`
Vector clustering with temporal color coding. Red = early in session, Blue = late in session.

![k-means color plot](/Resources/km_color.png)

#### `km_color_more.py`
Same as km_color.py but with finer decimation.

![k-means color more plot](/Resources/km_color_more.png)

#### `km_3d.py`
3D visualization with time as the Z-axis. Shows how subjects move through the maze over time.

![k-means 3d](/Resources/km_3d.png)

#### `km_avg.py`
3D representation of the **average path** for each cluster over time.

![k-means average](/Resources/km_avg.png)

### Educational

#### `failed_km.py`
A failed attempt at clustering kept for educational purposes. Demonstrates why creating 3D arrays from nested tuples doesn't work with sklearn.

```
ValueError: Found array with dim 3. Estimator expected <= 2.
```

## Configuration

All scripts use 8 clusters by default. Modify the `k` variable to change:

```python
k = 8  # Number of clusters
```

