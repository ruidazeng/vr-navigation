# Cluster Analysis on Subject Data in Immersive Virtual Environments

> **Contact:** Ruida Zeng — ruida dot zeng at vanderbilt dot edu

This repository contains work from the 2019 VUSE undergraduate summer research program at the **Learning in Virtual Environments (LIVE)** research lab at [Vanderbilt University's School of Engineering](https://engineering.vanderbilt.edu).

- **Graduate Research Assistant:** Richard Paris (VR environment creation in Unity, experiment conductor)
- **Primary Investigator:** [Dr. Bobby Bodenheimer](https://engineering.vanderbilt.edu/bio/robert-bodenheimer), Associate Professor, [EECS Department](https://engineering.vanderbilt.edu/eecs/)

## Overview

The project analyzes navigation patterns of ~200 subjects in an immersive virtual maze environment using k-means clustering and various visualization techniques.

![poster presentation](/Resources/poster.jpg)

## Project Structure

```
vr-navigation/
├── clustering/          # K-means clustering algorithms
├── visualization/       # Data visualization scripts  
├── preprocessing/       # Legacy data parsing scripts
├── Parsed Data/         # 143 parsed subject CSV files
└── Resources/           # Images and documentation
```

| Directory | Description | README |
|-----------|-------------|--------|
| [`clustering/`](clustering/) | K-means clustering scripts for subject navigation analysis | [View](clustering/README.md) |
| [`visualization/`](visualization/) | Matplotlib and turtle graphics visualizations | [View](visualization/README.md) |
| [`preprocessing/`](preprocessing/) | Legacy scripts for parsing raw experimental data | [View](preprocessing/README.md) |
| [`Parsed Data/`](Parsed%20Data/) | 143 parsed CSV files with subject navigation data | [View](Parsed%20Data/README.md) |

## Requirements

```
numpy
pandas
scikit-learn
matplotlib
```

Install with:
```bash
pip install numpy pandas scikit-learn matplotlib
```

## Quick Start

```bash
# Visualize a subject's navigation path
python visualization/visual.py

# Run k-means clustering on all subjects
python clustering/km_vector.py

# View 3D temporal clustering
python clustering/km_3d.py
```

## License

See [LICENSE](LICENSE) for details.
