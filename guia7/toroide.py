import pyvista as pv
import numpy as np
#Define los parametros del toro y sus nodos
radio = 2
n1 = 3
n2 = 7
#Define la funcion 3d para los nodos del toro
def nodos_toro(u, v):
    x = (radio + np.cos(n1 * u) * 0.5) * np.cos(n2 * v)
    y = (radio + np.cos(n1 * u) * 0.5) * np.sin(n2 * v)
    z = np.sin(n1 * u) * 0.5
    return x, y, z
#Crear una malla para la funcion 3d
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
x, y, z = nodos_toro(*np.meshgrid(u, v, indexing='ij'))
puntos = np.column_stack((x.ravel(), y.ravel(), z.ravel()))
mesh = pv.PolyData(puntos)
mesh.triangulate()
mesh = mesh.extract_surface()
# Visualizar la malla del toro
pv.plot(mesh, color='b', smooth_shading=True)