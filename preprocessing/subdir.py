"""
Iterate through raw data files to test the "find 10 min" algorithm.
Reports which files the algorithm successfully finds candidates for.

NOTE: This is a legacy script that requires external raw data files.
The data directory 'C:/Navigation Data/Labeled' is not included in this repository.
Update ROOTDIR to point to your local raw data directory.
"""
import os
import sys

# Configuration - update this path to point to your raw data directory
ROOTDIR = 'C:/Navigation Data/Labeled'

# Check if the required data directory exists
if not os.path.exists(ROOTDIR):
    print(f"ERROR: Required data directory '{ROOTDIR}' not found.")
    print("This script requires the original raw experimental data files.")
    print("Please update ROOTDIR at the top of this script to point to your data directory.")
    sys.exit(1)

works = 0
no_works = 0

for subdir, dirs, files in os.walk(ROOTDIR):
    for infile in files:
        if "CW4Test_Data" in infile:
            target_file = infile
        else:
            continue
        
        prev = 0
        started = False
        index = 0
        printed = False
        
        # Search for the magic 10 minutes
        with open(os.path.join(subdir, target_file)) as openfileobject:
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
                        if abs(prev - tracker) > 200 and abs(prev - tracker) < 700:
                            printed = True
                    started = not started
                prev = num
                index += 1
        
        # Report results
        # Handle both Windows and Unix path separators
        try:
            subject_id = subdir.split('\\')[-1] if '\\' in subdir else subdir.split('/')[-1]
        except IndexError:
            subject_id = subdir
        
        if printed:
            works += 1
            print('works:', subject_id)
        else:
            no_works += 1
            print("doesn't work:", subject_id)

print(f'\nwe successfully found candidate(s) for {works} files')
print(f'we failed to find any candidate for {no_works} files')
