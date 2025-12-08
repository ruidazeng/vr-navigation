# 🎨 Visualization Scripts

Scripts for visualizing subject navigation paths in the VR maze.

---

## 📋 Overview

| Script | Output | Description |
|--------|--------|-------------|
| [`visual.py`](#visualpy) | Static | Simple scatter plot of path |
| [`turtle_viz.py`](#turtle_vizpy) | Animated | Real-time path drawing |
| [`color_single.py`](#color_singlepy) | Static | Single subject, temporal colors |
| [`color_double.py`](#color_doublepy) | Static | Two subjects comparison |

---

## 📊 Basic Visualization

### `visual.py`

Simple scatter plot of a subject's navigation path using matplotlib.

```bash
python visualization/visual.py
```

<p align="center">
  <img src="../Resources/visual.png" alt="Visual Plot" width="500"/>
</p>

---

## 🐢 Animated Visualization

### `turtle_viz.py`

Animated visualization using Python's turtle graphics module. Draws the navigation path in **real-time**, showing the subject's movement through the maze.

```bash
python visualization/turtle_viz.py
```

<p align="center">
  <img src="../Resources/turtle.png" alt="Turtle Plot" width="500"/>
</p>

> 💡 **Tip:** This is great for presentations and understanding movement patterns intuitively.

---

## 🌈 Temporal Color Coding

Color represents time progression through the 10-minute session:

| Color | Meaning |
|-------|---------|
| 🔴 **Red** | Early in session (start) |
| 🔵 **Blue** | Late in session (end) |

### `color_single.py`

Visualize a **single subject's** path with temporal color coding.

```bash
python visualization/color_single.py
```

<p align="center">
  <img src="../Resources/1color.png" alt="Single Color Plot" width="500"/>
</p>

---

### `color_double.py`

Compare **two subjects'** paths side-by-side with temporal color coding.

```bash
python visualization/color_double.py
```

<p align="center">
  <img src="../Resources/2color.png" alt="Double Color Plot" width="500"/>
</p>

---

## ⚙️ Configuration

### Single Subject Scripts

Modify the `filename` variable to visualize different subjects:

```python
filename = 'AAAA.csv'  # Change to any CSV in Parsed Data/
```

### Comparison Script

For `color_double.py`, modify both filenames:

```python
filename1 = 'AAAA.csv'  # First subject
filename2 = 'ACGN.csv'  # Second subject
```

---

## 🎯 Which Script to Use?

```
Need a quick look at a path?
    └── Use visual.py

Want to understand movement over time?
    └── Use color_single.py

Comparing two subjects?
    └── Use color_double.py

Giving a presentation or demo?
    └── Use turtle_viz.py (animated!)
```

---

<p align="center">
  <a href="../README.md">⬅️ Back to Main README</a>
</p>
