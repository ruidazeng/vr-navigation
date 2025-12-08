"""
Generate a CSV file from raw tab-separated experimental data.
Applies the "find 10 min" slicing algorithm to extract useful navigation data.

NOTE: This is a legacy script that requires external raw data files.
The raw data file 'CW4Test_Data.txt' is not included in this repository.
"""
import os
import sys
import pandas as pd

# Configuration - update this path to point to your raw data file
FILENAME = 'CW4Test_Data.txt'

# Check if the required data file exists
if not os.path.exists(FILENAME):
    print(f"ERROR: Required data file '{FILENAME}' not found.")
    print("This script requires the original raw experimental data file.")
    print("Please place the raw data file in the current directory and try again.")
    sys.exit(1)

prev = 0
started = False
index = 0
unique_start_index = None
unique_end_index = None

# Search for the magic 10 minutes
with open(FILENAME) as openfileobject:
    for line in openfileobject:
        # Skip blank lines
        if line == '\n':
            continue
        datetime = line.split('\t')[0]
        num = float(line.split('\t')[1])
        
        if index == 0:
            prev = num
            index += 1
            continue
        
        # This code ensures only around-10 minutes intervals are found
        if abs(num - prev) > 1.00:
            if not started:
                tracker = num
                start_index = index
                start_datetime = datetime
                start_prev = prev
                start_num = num
            else:
                end_index = index
                end_datetime = datetime
                end_prev = prev
                end_num = num
                if abs(prev - tracker) > 200 and abs(prev - tracker) < 700:
                    print('start of 10 minutes:')
                    print('index:', start_index, '\ntime stamp:', start_datetime, '---', start_prev, start_num, '\n')
                    print('end of 10 minutes:')
                    print('index:', end_index, '\ntime stamp:', end_datetime, '---', end_prev, end_num, '\n')
                    
                    # Store unique indices
                    unique_start_index = start_index
                    unique_end_index = end_index
            
            started = not started
        prev = num
        index += 1

# Check if we found valid 10-minute segment
if unique_start_index is None or unique_end_index is None:
    print("ERROR: Could not find a valid 10-minute segment in the data.")
    sys.exit(1)

# Shift to get the learning maze (not training maze)
unique_start_index = unique_end_index
unique_end_index = unique_start_index + 30000

duration = unique_end_index - unique_start_index

# Read in the tab-separated values
df = pd.read_csv(
    FILENAME,
    sep='\t',
    lineterminator='\n',
    header=None,
    skiprows=unique_start_index,
    nrows=duration,
    names=['date/time', 'seconds since started', 'is button down?',
           'accelX', 'accelY', 'accelZ', 'posX', 'posY', 'posZ', 'rotX', 'rotY', 'rotZ']
)

# Parse only the useful variables
df = df[['date/time', 'seconds since started', 'posX', 'posY', 'posZ', 'rotX', 'rotY', 'rotZ']]

print(df.shape)
print('finish loading into pandas')

# Visualize the result
import matplotlib.pyplot as plt

df.plot(kind='scatter', x='posX', y='posZ', color='red')
plt.title('Parsed Navigation Data')
plt.show()

# Export to CSV
output_filename = 'export_dataframe.csv'
df.to_csv(output_filename, index=None, header=True)
print(f'Exported to {output_filename}')
