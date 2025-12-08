"""
Visual representation using turtle module (live animation).
"""
import os
import pandas as pd
from turtle import speed, color, setpos, goto, dot, done

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, 'Parsed Data')

filename = 'AAAA.csv'

# Read CSV file
filepath = os.path.join(DATA_DIR, filename)
df = pd.read_csv(filepath, sep=',', lineterminator='\n')

print(df.shape)
print('finish loading into pandas')

# Decimate data for visualization
df = df[df.index % 30 == 0]

# Setup turtle
speed(10)
color('olive')

# Draw path
setpos(df['posZ'].iloc[0] * 50, df['posX'].iloc[0] * -50)
for index, row in df.iterrows():
    goto(df['posZ'].loc[index] * 50, df['posX'].loc[index] * -50)
    dot()
done()

print('done')
