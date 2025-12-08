"""
Visual representation of two CSV files with temporal color coding.
Red indicates early, blue indicates late.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, 'Parsed Data')

filename1 = 'AAAA.csv'
filename2 = 'ACGN.csv'

# Read CSV files
df1 = pd.read_csv(os.path.join(DATA_DIR, filename1), sep=',', lineterminator='\n')
df2 = pd.read_csv(os.path.join(DATA_DIR, filename2), sep=',', lineterminator='\n')

print('finish loading into pandas')

# Extract position data (decimated)
X1 = df1['posX'].values[0:30000:10]
Y1 = df1['posZ'].values[0:30000:10]
X2 = df2['posX'].values[0:30000:10]
Y2 = df2['posZ'].values[0:30000:10]

# Create color gradient (red=early, blue=late)
colorGrad = [[i / 3000, 0, 1 - i / 3000] for i in range(3000)]

# Plot scatter with temporal color coding
plt.scatter(X1, Y1, c=colorGrad)
plt.scatter(X2, Y2, c=colorGrad)
plt.xlabel('posX')
plt.ylabel('posZ')
plt.title(f'Navigation Paths: {filename1} and {filename2}')
plt.show()
