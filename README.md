<p align="center">
  <img src="Resources/maze.png" alt="VR Maze Environment" width="500"/>
</p>

<h1 align="center">🧭 VR Navigation Analysis</h1>

---

<p align="center">
  <b>Cluster Analysis on Subject Data in Immersive Virtual Environments</b>
</p>

<p align="center">
  <i>A framework for analyzing navigation patterns in virtual reality environments</i><br/>
  <i>using k-means clustering to identify behavioral strategies in maze exploration</i>
</p>

<p align="center">
  <i>Ruida Zeng, Richard Paris, Bobby Bodenheimer</i>
</p>

<p align="center">
  <i><a href="https://engineering.vanderbilt.edu">Learning in Virtual Environments (LIVE) Lab</a>, Vanderbilt University</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python"/>
  <img src="https://img.shields.io/badge/NumPy-1.19+-green.svg" alt="NumPy"/>
  <img src="https://img.shields.io/badge/scikit--learn-0.24+-orange.svg" alt="scikit-learn"/>
  <img src="https://img.shields.io/badge/License-See%20LICENSE-lightgrey.svg" alt="License"/>
</p>

<p align="center">
  <a href="#overview">Overview</a> •
  <a href="#team">Team</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#results">Results</a> •
  <a href="#project-structure">Structure</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#documentation">Documentation</a>
</p>

---

## Overview

Analysis of navigation patterns from **~200 subjects** in an immersive virtual maze environment. This research was conducted during the **2019 VUSE Undergraduate Summer Research Program**.

The project applies **k-means clustering** to identify distinct navigation strategies and behavioral patterns as subjects explore and learn a virtual maze over 10-minute sessions.

<p align="center">
  <img src="Resources/poster.jpg" alt="Research Poster" width="650"/>
</p>

---

## Team

| Role | Name | Contribution |
|------|------|--------------|
| **Primary Investigator** | [Dr. Bobby Bodenheimer](https://engineering.vanderbilt.edu/bio/robert-bodenheimer) | Project oversight, [EECS Department](https://engineering.vanderbilt.edu/eecs/) |
| **Graduate Research Assistant** | Richard Paris | VR environment creation (Unity), experiment design |
| **Undergraduate Researcher** | Ruida Zeng | Data analysis, clustering algorithms |

> 📧 **Contact:** ruida dot zeng at vanderbilt dot edu

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ruidazeng/vr-navigation.git
cd vr-navigation

# Install dependencies
pip install -r requirements.txt
```

### Run Examples

```bash
# Visualize a subject's navigation path
python visualization/visual.py

# Run k-means clustering on all subjects
python clustering/km_vector.py

# View 3D temporal clustering
python clustering/km_3d.py
```

---

## Results

<table>
  <tr>
    <td align="center">
      <img src="Resources/km_vector.png" width="280"/><br/>
      <sub><b>K-Means Clustering</b></sub>
    </td>
    <td align="center">
      <img src="Resources/km_3d.png" width="280"/><br/>
      <sub><b>3D Temporal View</b></sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="Resources/km_color.png" width="280"/><br/>
      <sub><b>Temporal Color Coding</b></sub>
    </td>
    <td align="center">
      <img src="Resources/visual.png" width="280"/><br/>
      <sub><b>Path Visualization</b></sub>
    </td>
  </tr>
</table>

---

## Project Structure

```
vr-navigation/
├── clustering/          # K-means clustering algorithms
├── visualization/       # Data visualization scripts  
├── preprocessing/       # Legacy data parsing scripts
├── Parsed Data/         # 143 subject CSV files
└── Resources/           # Images and documentation
```

| Directory | Description | Docs |
|-----------|-------------|------|
| [`clustering/`](clustering/) | K-means clustering for navigation pattern analysis | [📖 README](clustering/README.md) |
| [`visualization/`](visualization/) | Matplotlib and turtle graphics visualizations | [📖 README](visualization/README.md) |
| [`preprocessing/`](preprocessing/) | Legacy scripts for parsing raw experimental data | [📖 README](preprocessing/README.md) |
| [`Parsed Data/`](Parsed%20Data/) | 143 parsed CSV files with subject navigation data | [📖 README](Parsed%20Data/README.md) |

---

## Requirements

| Package | Version | Purpose |
|---------|---------|---------|
| `numpy` | 1.19+ | Numerical computing |
| `pandas` | 1.0+ | Data manipulation |
| `scikit-learn` | 0.24+ | K-means clustering |
| `matplotlib` | 3.3+ | Visualization |

```bash
pip install -r requirements.txt
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [Clustering Scripts](clustering/README.md) | K-means algorithms and usage |
| [Visualization Scripts](visualization/README.md) | Path visualization tools |
| [Preprocessing Scripts](preprocessing/README.md) | Legacy data parsing documentation |
| [Parsed Data](Parsed%20Data/README.md) | Data format and subject status |
| [LICENSE](LICENSE) | License information |

---

<p align="center">
  <sub>Made with ❤️ at Vanderbilt University • 2019 Summer Research</sub>
</p>
