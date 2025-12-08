# Visualization Scripts

Scripts for visualizing subject navigation paths in the VR maze.

## Scripts

### `visual.py`
Simple scatter plot of subject path using matplotlib.

```bash
python visualization/visual.py
```

![visual plot](/Resources/visual.png)

### `turtle_viz.py`
Animated visualization using Python's turtle graphics module. Draws the navigation path in real-time.

```bash
python visualization/turtle_viz.py
```

![turtle plot](/Resources/turtle.png)

### `color_single.py`
Temporal color-coded visualization of a single subject's path.
- 🔴 Red = Early in session
- 🔵 Blue = Late in session

```bash
python visualization/color_single.py
```

![one color](/Resources/1color.png)

### `color_double.py`
Compare two subjects' paths side-by-side with temporal color coding.

```bash
python visualization/color_double.py
```

![two color](/Resources/2color.png)

## Configuration

To visualize a different subject, modify the `filename` variable:

```python
filename = 'AAAA.csv'  # Change to any CSV in Parsed Data/
```

For `color_double.py`, modify both:
```python
filename1 = 'AAAA.csv'
filename2 = 'ACGN.csv'
```

