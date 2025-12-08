# 🧭 VR Navigation Analysis

> **Cluster Analysis on Subject Data in Immersive Virtual Environments**

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-See%20LICENSE-green.svg)](LICENSE)

This repository contains research from the **2019 VUSE Undergraduate Summer Research Program** at the [Learning in Virtual Environments (LIVE)](https://engineering.vanderbilt.edu) lab, Vanderbilt University.

<p align="center">
  <img src="Resources/maze.png" alt="VR Maze Environment" width="400"/>
</p>

## 👥 Team

| Role | Name | Contribution |
|------|------|--------------|
| **Primary Investigator** | [Dr. Bobby Bodenheimer](https://engineering.vanderbilt.edu/bio/robert-bodenheimer) | Project oversight, EECS Department |
| **Graduate Research Assistant** | Richard Paris | VR environment creation (Unity), experiment design |
| **Undergraduate Researcher** | Ruida Zeng | Data analysis, clustering algorithms |

> 📧 **Contact:** ruida dot zeng at vanderbilt dot edu

---

## 📊 Overview

Analysis of navigation patterns from **~200 subjects** in an immersive virtual maze environment using k-means clustering and visualization techniques.

<p align="center">
  <img src="Resources/poster.jpg" alt="Research Poster" width="600"/>
</p>

---

## 📁 Project Structure

```
vr-navigation/
├── 📂 clustering/        # K-means clustering algorithms
├── 📂 visualization/     # Data visualization scripts  
├── 📂 preprocessing/     # Legacy data parsing scripts
├── 📂 Parsed Data/       # 143 subject CSV files
└── 📂 Resources/         # Images and documentation
```

| Directory | Description | Docs |
|-----------|-------------|------|
| [`clustering/`](clustering/) | K-means clustering for navigation pattern analysis | [📖 README](clustering/README.md) |
| [`visualization/`](visualization/) | Matplotlib and turtle graphics visualizations | [📖 README](visualization/README.md) |
| [`preprocessing/`](preprocessing/) | Legacy scripts for parsing raw experimental data | [📖 README](preprocessing/README.md) |
| [`Parsed Data/`](Parsed%20Data/) | 143 parsed CSV files with subject navigation data | [📖 README](Parsed%20Data/README.md) |

---

## ⚡ Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/vr-navigation.git
cd vr-navigation

# Install dependencies
pip install -r requirements.txt
```

### Run Examples

```bash
# 🎨 Visualize a subject's navigation path
python visualization/visual.py

# 🔬 Run k-means clustering on all subjects
python clustering/km_vector.py

# 📈 View 3D temporal clustering
python clustering/km_3d.py
```

---

## 🔧 Requirements

| Package | Purpose |
|---------|---------|
| `numpy` | Numerical computing |
| `pandas` | Data manipulation |
| `scikit-learn` | K-means clustering |
| `matplotlib` | Visualization |

---

## 🖼️ Sample Results

<table>
  <tr>
    <td align="center">
      <img src="Resources/km_vector.png" width="300"/><br/>
      <sub><b>K-Means Clustering</b></sub>
    </td>
    <td align="center">
      <img src="Resources/km_3d.png" width="300"/><br/>
      <sub><b>3D Temporal View</b></sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="Resources/km_color.png" width="300"/><br/>
      <sub><b>Temporal Color Coding</b></sub>
    </td>
    <td align="center">
      <img src="Resources/visual.png" width="300"/><br/>
      <sub><b>Path Visualization</b></sub>
    </td>
  </tr>
</table>

---

## 📜 License

See [LICENSE](LICENSE) for details.

---

<p align="center">
  <sub>Made with ❤️ at Vanderbilt University • 2019 Summer Research</sub>
</p>
