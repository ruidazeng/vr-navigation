# Preprocessing Scripts (Legacy)

These scripts were used to parse the original raw experimental data files into the clean CSV format found in `Parsed Data/`.

> ⚠️ **Note:** These scripts require the original raw data files which are **not included** in this repository. They will display helpful error messages if run without the required data.

## Scripts

### `makecsv.py`
Generates a clean CSV file from the original tab-separated `.txt` file using the "find 10 min" slicing algorithm.

**Required input:** `CW4Test_Data.txt` (raw experimental data)

### `matplotfullalgo.py`
Visualizes a 10-minute slot found by the slicing algorithm. Used to verify the algorithm found the correct navigation segment.

### `subdir.py`
Iterates through all raw data files to test the "find 10 min" algorithm. Reports which files the algorithm works on.

### `subdir_multiple.py`
Identifies files where the algorithm found **two or more** candidate 10-minute segments (ambiguous cases).

### `subdir_unique.py`
Identifies files where the algorithm found **exactly one** candidate (ideal cases).

## The "Find 10 Min" Algorithm

The raw experimental data contains:
1. Training maze session
2. Learning maze session (the 10 minutes we want)
3. Other calibration/setup data

The algorithm detects time gaps in the data to identify the 10-minute learning maze segment. See the [Parsed Data README](../Parsed%20Data/README.md) for details on which subjects required manual intervention.

## Configuration

To use these scripts with your own raw data:

1. Update the `FILENAME` or `ROOTDIR` variable at the top of each script
2. Ensure raw data files follow the expected tab-separated format:
   ```
   date/time  seconds  is_button_down  accelX  accelY  accelZ  posX  posY  posZ  rotX  rotY  rotZ
   ```

