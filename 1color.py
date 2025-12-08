import os
import pandas as pd
import matplotlib.pyplot as plt

# Configuration
DATA_DIR = 'Parsed Data'
filename = 'AAAA.csv'

# Read CSV file
filepath = os.path.join(DATA_DIR, filename)
df = pd.read_csv(filepath, sep=',', lineterminator='\n')

print('finish loading into pandas')

# Extract position data (decimated)
X = df['posX'].values[0:30000:10]
Y = df['posZ'].values[0:30000:10]

# Create color gradient (red=early, blue=late)
colorGrad = [[i / 3000, 0, 1 - i / 3000] for i in range(3000)]

# Plot scatter with temporal color coding
plt.scatter(X, Y, c=colorGrad)
plt.xlabel('posX')
plt.ylabel('posZ')
plt.title(f'Navigation Path: {filename}')
plt.show()
