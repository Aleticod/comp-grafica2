import pyvista as pv
import numpy as np
#Define los parametros del hiperboloide y sus nodos
a = 2
b = 2
c = 2
#Define la funcion 3d para los nodos del hiperboloide
def nodos_hiperboloide(u, v):
    x = a * (np.cosh(u)) * np.cos(v)
    y = b * (np.cosh(u)) * np.sin(v)
    z = c * np.sinh(u)
    return x, y, z
#Crear una malla para la funcion 3d
u = np.linspace(-2, 2, 100)
v = np.linspace(0, 2 * np.pi, 100)
x, y, z = nodos_hiperboloide(*np.meshgrid(u, v, indexing='ij'))
puntos = np.column_stack((x.ravel(), y.ravel(), z.ravel()))
mesh = pv.PolyData(puntos)
mesh.triangulate()
mesh = mesh.extract_surface()
# Visualizar la malla del hiperboloide
pv.plot(mesh, color='b', smooth_shading=True)