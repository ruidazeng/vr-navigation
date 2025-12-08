"""
Identify files where the "find 10 min" algorithm found TWO OR MORE candidates.
This helps identify ambiguous cases that may need manual review.

NOTE: This is a legacy script that requires external raw data files.
The data directory 'C:/Navigation Data/Labeled' is not included in this repository.
Update ROOTDIR to point to your local raw data directory.
"""
import os
import sys
import traceback

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
    try:
        for infile in files:
            if "CW4Test_Data" in infile:
                target_file = infile
            else:
                continue
            
            prev = 0
            started = False
            index = 0
            printed = 0  # Count of candidates found
            
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
                                printed += 1
                        started = not started
                    prev = num
                    index += 1
            
            # Report results - looking for files with MULTIPLE candidates
            # Handle both Windows and Unix path separators
            try:
                subject_id = subdir.split('\\')[-1] if '\\' in subdir else subdir.split('/')[-1]
            except IndexError:
                subject_id = subdir
            
            if printed > 1:
                works += 1
                print(f'multiple candidates ({printed}):', subject_id)
            else:
                no_works += 1
                print("doesn't have multiple:", subject_id)
    except Exception:
        no_works += 1
        try:
            subject_id = subdir.split('\\')[-1] if '\\' in subdir else subdir.split('/')[-1]
        except IndexError:
            subject_id = subdir
        print('exception detected:', subject_id)
        print('\n', traceback.format_exc())

print(f'\nwe found multiple candidates for {works} files')
print(f'we did not find multiple candidates for {no_works} files')
