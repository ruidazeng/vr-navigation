"""
Visual representation using matplotlib module.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

# Configuration
DATA_DIR = 'Parsed Data'
filename = 'AAAA.csv'

# Read CSV file
filepath = os.path.join(DATA_DIR, filename)
df = pd.read_csv(filepath, sep=',', lineterminator='\n')

print(df.shape)
print('finish loading into pandas')

# Plot scatter
df.plot(kind='scatter', x='posX', y='posZ', color='olive')
plt.title(f'Navigation Path: {filename}')
plt.show()
