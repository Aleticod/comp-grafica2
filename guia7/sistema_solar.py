import pyvista
import math
import numpy as np

#creamos una esfera
esfera = pyvista.Sphere(radius=1, theta_resolution=120, phi_resolution=120, start_theta=270.001,
end_theta=270)
esfera.active_t_coords = np.zeros((esfera.points.shape[0], 2))

#definimos las ecuaciones UV para el mapeo de una esfera
esfera.active_t_coords[:, 0] = 0.5 + np.arctan2(-esfera.points[:, 0], esfera.points[:,1])/(2 * math.pi)
esfera.active_t_coords[:, 1] = 0.5 + np.arcsin(esfera.points[:, 2]) / math.pi
esfera0 = esfera.copy()
esfera0.points *= 2.2
esfera0.points += [21.0, 0.0, 19.0]
esfera1 = esfera.copy()
esfera1.points *= 1.2
esfera1.points += [16.5, 0.0, 18.0]
esfera2 = esfera.copy()
esfera2.points *= 1.4
esfera2.points += [14.0, 0.0, 16.5]
esfera3 = esfera.copy()
esfera3.points *= 2
esfera3.points += [11.5, 0.0, 14.0]
esfera31 = esfera.copy()
esfera31.points *= 0.5
esfera31.points += [9.0, 0.0, 15.8]
esfera4 = esfera.copy()
esfera4.points *= 1.7
esfera4.points += [8.8, 0.0, 11]
esfera5 = esfera.copy()
esfera5.points *= 5
esfera5.points += [3.0, 0.0, 7]
esfera6 = esfera.copy()
esfera6.points *= 3.5
esfera6.points += [-2.0, 0.0, -1.0]
esfera7 = esfera.copy()
esfera7.points *= 2
esfera7.points += [-7.0, 0.0, -6.9]
esfera8 = esfera.copy()
esfera8.points *= 2.6
esfera8.points += [-12, 0.0, -11.5]

# Creamos el anillo alrededor de la esfera
radio_anillo = 6.0 # Tamaño del anillo

theta = np.linspace(0, 2*np.pi, 300)

# Genramos el anillo
x_anillo = radio_anillo * np.cos(theta)
y_anillo = radio_anillo * np.sin(theta)
z_anillo = np.zeros_like(x_anillo)
anillo = pyvista.PolyData(np.column_stack([x_anillo, y_anillo, z_anillo]))
anillo1 = anillo.copy()
anillo1.points += [-2.0, 0.0, -1.0]
anillo2 = anillo.copy()
anillo2.points *= 1.2
anillo2.points += [-2.0, 0.0, -1.0]

#asignamos la textura y mostramos la imagen
sol = pyvista.Texture("Sol.jpeg")
mercurio = pyvista.Texture("Mercurio.jpeg")
venus = pyvista.Texture("Venus.jpeg")
tierra = pyvista.Texture("Tierra.jpg")
luna = pyvista.Texture("Luna.jpeg")
marte = pyvista.Texture("Marte.jpg")
jupiter = pyvista.Texture("Jupiter.jpg")
saturno = pyvista.Texture("Saturno.jpg")
urano = pyvista.Texture("Urano.jpg")
neptuno = pyvista.Texture("Neptuno.jpg")
pl = pyvista.Plotter()
pl.add_background_image("estrellas.jpg")

# renderizamos la textura
pl.add_mesh(esfera0, texture=sol, smooth_shading=False)
pl.add_mesh(esfera1, texture=mercurio, smooth_shading=False)
pl.add_mesh(esfera2, texture=venus, smooth_shading=False)
pl.add_mesh(esfera3, texture=tierra, smooth_shading=False)
pl.add_mesh(esfera31, texture=luna, smooth_shading=False)
pl.add_mesh(esfera4, texture=marte, smooth_shading=False)
pl.add_mesh(esfera5, texture=jupiter, smooth_shading=False)
pl.add_mesh(esfera6, texture=saturno, smooth_shading=False)
pl.add_mesh(anillo1, color=[0.5,0.5,0.5], line_width=3)
pl.add_mesh(anillo2, color=[0.5,0.5,0.5], line_width=3)
pl.add_mesh(esfera7, texture=urano, smooth_shading=False)
pl.add_mesh(esfera8, texture=neptuno, smooth_shading=False)
pl.camera_position = [(10, 60, 10), (5, -1, 5), (0, 2, 1)]
pl.show()