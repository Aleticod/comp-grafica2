import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# Define vertices del icosaedro
PHI = (1 + 5**0.5) / 2
vertices = np.array([
    [-1, PHI, 0],
    [1, PHI, 0],
    [-1, -PHI, 0],
    [1, -PHI, 0],
    [0, -1, PHI],
    [0, 1, PHI],
    [0, -1, -PHI],
    [0, 1, -PHI],
    [PHI, 0, -1],
    [PHI, 0, 1],
    [-PHI, 0, -1],
    [-PHI, 0, 1],
])
# Define indices (triangulos) del icosaedro
indices = np.array([
    [0, 11, 5],
    [0, 5, 1],
    [0, 1, 7],
    [0, 7, 10],
    [0, 10, 11],
    [1, 5, 9],
    [5, 11, 4],
    [11, 10, 2],
    [10, 7, 6],
    [7, 1, 8],
    [3, 9, 4],
    [3, 4, 2],
    [3, 2, 6],
    [3, 6, 8],
    [3, 8, 9],
    [4, 9, 5],
    [2, 4, 11],
    [6, 2, 10],
    [8, 6, 7],
    [9, 8, 1],
    [1, 5, 0],
    [5, 11, 0],
    [11, 10, 0],
    [10, 7, 0],
    [7, 1, 0],
    [5, 9, 1],
    [11, 4, 5],
    [10, 2, 11],
    [7, 6, 10],
    [1, 8, 7],
    [9, 4, 3],
    [4, 2, 3],
    [2, 6, 3],
    [6, 8, 3],
    [8, 9, 3],
    [9, 5, 4],
    [4, 11, 2],
    [2, 10, 6],
    [6, 7, 8],
    [8, 1, 9]
])
# Visualizamos la malla del icosaedro
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for triangulo in indices:
    ax.plot(vertices[triangulo, 0], vertices[triangulo, 1], vertices[triangulo, 2],'b-')
plt.show()