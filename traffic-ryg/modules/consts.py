import numpy as np

DISTANCES = np.full((6,6), -1)

for i in range(6):
    for j in range(i+1, 6):
        DISTANCES[i, j] = np.random.randint(1, 4)