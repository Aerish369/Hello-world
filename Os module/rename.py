import os

for i in range(0, 10):
    os.rename(f"data/Tutorial{i+1}", f"data/Day {i+1}")