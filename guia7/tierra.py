import pyvista
import math
import numpy as np
#creamos una esfera
esfera = pyvista.Sphere(radius=1, theta_resolution=120, phi_resolution=120, start_theta=270.001, end_theta=270)
esfera.active_t_coords = np.zeros((esfera.points.shape[0], 2))
#definimos las ecuaciones UV para el mapeo de una esfera
esfera.active_t_coords[:, 0] = 0.5 + np.arctan2(-esfera.points[:, 0], esfera.points[:,
1])/(2 * math.pi)
esfera.active_t_coords[:, 1] = 0.5 + np.arcsin(esfera.points[:, 2]) / math.pi
#asignamos la textura y mostramos la imagen
tierra = pyvista.Texture("Tierra.jpg")
pl = pyvista.Plotter()
pl.add_mesh(esfera, texture=tierra, smooth_shading=False)
pl.show()