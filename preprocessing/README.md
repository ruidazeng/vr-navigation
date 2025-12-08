# 🔧 Preprocessing Scripts

Legacy scripts used to parse raw experimental data into the clean CSV format.

> ⚠️ **Legacy Code:** These scripts require the original raw data files which are **not included** in this repository. They are preserved for documentation purposes.

---

## 📋 Overview

| Script | Purpose |
|--------|---------|
| [`makecsv.py`](#makecsvpy) | Convert raw `.txt` to clean `.csv` |
| [`matplotfullalgo.py`](#matplotfullalgopy) | Visualize algorithm results |
| [`subdir.py`](#subdirpy) | Test algorithm on all files |
| [`subdir_multiple.py`](#subdir_multiplepy) | Find ambiguous cases |
| [`subdir_unique.py`](#subdir_uniquepy) | Find ideal cases |

---

## 🧮 The "Find 10 Min" Algorithm

The raw experimental data contains multiple segments:

```
┌─────────────────────────────────────────────────────────┐
│  Raw Data File                                          │
├─────────────────────────────────────────────────────────┤
│  1. Calibration/Setup      │  ❌ Not needed            │
│  2. Training Maze          │  ❌ Not needed            │
│  3. Learning Maze (10 min) │  ✅ TARGET DATA           │
│  4. Other sessions         │  ❌ Not needed            │
└─────────────────────────────────────────────────────────┘
```

The algorithm **detects time gaps** in the data to identify and extract the 10-minute learning maze segment.

---

## 📜 Scripts

### `makecsv.py`

Converts a single raw tab-separated `.txt` file to a clean CSV using the slicing algorithm.

**Required Input:** `CW4Test_Data.txt` (raw experimental data)

```python
# Input format (tab-separated):
# date/time  seconds  is_button_down  accelX  accelY  accelZ  posX  posY  posZ  rotX  rotY  rotZ

# Output format (CSV):
# date/time,seconds since started,posX,posY,posZ,rotX,rotY,rotZ
```

---

### `matplotfullalgo.py`

Visualizes the 10-minute slot found by the algorithm. Used to **verify correctness** by visual inspection.

```
✓ Correct: Shows learning maze pattern
✗ Incorrect: Shows training maze or nonsense data
```

---

### `subdir.py`

Iterates through **all raw data files** to test algorithm effectiveness. Reports success/failure for each file.

---

### `subdir_multiple.py`

Identifies files where the algorithm found **2+ candidate** 10-minute segments (ambiguous cases requiring manual review).

---

### `subdir_unique.py`

Identifies files where the algorithm found **exactly 1 candidate** (ideal cases, no manual intervention needed).

---

## 📊 Processing Results

See the [Parsed Data README](../Parsed%20Data/README.md#-subject-processing-status) for the complete table of which subjects required manual intervention.

**Summary:**

| Status | Count | Description |
|--------|-------|-------------|
| **V/Y** | ~45 | Parsed perfectly |
| **N** | ~80 | Required 10-min shift |
| **X** | ~20 | Discarded (unusable) |

---

## 🔄 Raw Data Format

If you have similar raw data to process:

```
Column        Description
──────────    ─────────────────────────
date/time     Timestamp
seconds       Seconds since recording start
is_button     Button press state
accelX/Y/Z    Accelerometer data
posX/Y/Z      Position in 3D space
rotX/Y/Z      Head rotation (Euler angles)
```

**Configuration:**

1. Update `FILENAME` or `ROOTDIR` at the top of each script
2. Ensure raw data follows the tab-separated format above

---

<p align="center">
  <a href="../README.md">⬅️ Back to Main README</a>
</p>
