# 🔬 Clustering Scripts

K-means clustering algorithms for analyzing subject navigation patterns in VR maze data.

---

## 📋 Overview

| Script | Type | Description |
|--------|------|-------------|
| [`km_linear.py`](#km_linearpy) | Single Subject | Basic position clustering |
| [`km_quadruple.py`](#km_quadruplepy) | Multi-Subject | Decision point analysis |
| [`km_vector.py`](#km_vectorpy) | Multi-Subject | Path similarity clustering |
| [`km_vector_more.py`](#km_vector_morepy) | Multi-Subject | High-resolution path clustering |
| [`km_color.py`](#km_colorpy) | Visualization | Temporal color-coded clusters |
| [`km_color_more.py`](#km_color_morepy) | Visualization | High-res temporal clustering |
| [`km_3d.py`](#km_3dpy) | Visualization | 3D temporal view |
| [`km_avg.py`](#km_avgpy) | Visualization | Average cluster paths |
| [`failed_km.py`](#failed_kmpy) | Educational | Failed attempt (kept for learning) |

---

## 🎯 Single Subject Analysis

### `km_linear.py`

Basic k-means clustering on `(posX, posZ)` position tuples for a single subject. Identifies spatial regions where the subject spent time in the maze.

```bash
python clustering/km_linear.py
```

<p align="center">
  <img src="../Resources/km_linear.png" alt="K-means Linear Plot" width="500"/>
</p>

---

## 👥 Multi-Subject Analysis

### `km_quadruple.py`

Clusters subjects based on **time spent at 4 decision points** (maze intersections). Creates a 4-dimensional feature vector representing hesitation time at each intersection.

```bash
python clustering/km_quadruple.py
```

**Decision Point Coordinates:**

| Intersection | X | Z |
|-------------|---|---|
| 1 | -2.5 | 2.1 |
| 2 | -1.1 | -2.0 |
| 3 | 1.5 | -2.5 |
| 4 | 1.9 | 1.35 |

<p align="center">
  <img src="../Resources/km_quadruple.png" alt="K-means Quadruple Plot" width="500"/>
</p>

---

### `km_vector.py`

Creates **60-element feature vectors** (30 decimated X + 30 Z positions) per subject, then clusters subjects by navigation similarity.

```bash
python clustering/km_vector.py
```

> ⚠️ **Note:** Excludes 2 files due to decimation requirements.

<p align="center">
  <img src="../Resources/km_vector.png" alt="K-means Vector Plot" width="500"/>
</p>

---

### `km_vector_more.py`

Same approach with finer decimation (every 10th point). Creates **6000-element vectors** for higher resolution clustering.

```bash
python clustering/km_vector_more.py
```

> ⚠️ **Note:** Excludes 39 files due to stricter size requirements.

<p align="center">
  <img src="../Resources/km_vector_more.png" alt="K-means Vector More Plot" width="500"/>
</p>

---

## 🎨 Temporal Visualizations

### `km_color.py`

Vector clustering with temporal color coding showing progression through the session.

```bash
python clustering/km_color.py
```

| Color | Meaning |
|-------|---------|
| 🔴 Red | Early in session |
| 🔵 Blue | Late in session |

<p align="center">
  <img src="../Resources/km_color.png" alt="K-means Color Plot" width="500"/>
</p>

---

### `km_color_more.py`

Same as `km_color.py` but with finer decimation for higher resolution.

```bash
python clustering/km_color_more.py
```

<p align="center">
  <img src="../Resources/km_color_more.png" alt="K-means Color More Plot" width="500"/>
</p>

---

### `km_3d.py`

3D visualization with **time as the Z-axis**. Shows how subjects move through the maze over the duration of the session.

```bash
python clustering/km_3d.py
```

<p align="center">
  <img src="../Resources/km_3d.png" alt="K-means 3D Plot" width="500"/>
</p>

---

### `km_avg.py`

3D representation of the **average path** for each cluster over time. Useful for identifying typical navigation strategies.

```bash
python clustering/km_avg.py
```

<p align="center">
  <img src="../Resources/km_avg.png" alt="K-means Average Plot" width="500"/>
</p>

---

## 📚 Educational

### `failed_km.py`

A failed clustering attempt preserved for educational purposes. Demonstrates why creating 3D arrays from nested tuples doesn't work with scikit-learn.

```python
# This produces:
ValueError: Found array with dim 3. Estimator expected <= 2.
```

**Lesson:** Always flatten nested structures before passing to sklearn estimators.

---

## ⚙️ Configuration

All scripts use **8 clusters** by default. Modify the `k` variable to experiment:

```python
k = 8  # Number of clusters - try different values!
```

---

<p align="center">
  <a href="../README.md">⬅️ Back to Main README</a>
</p>
