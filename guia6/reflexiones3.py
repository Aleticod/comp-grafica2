# Importamos librerias
import numpy as np
import matplotlib.pyplot as plt

# Funcion para normalizar un vector
def normalizar(vector):
    return vector / np.linalg.norm(vector)

# Funcion que devuelve vector reflejado
def reflejado(vector, eje):
    return vector - 2 * np.dot(vector, eje) * eje

# Funcion de interseccion con la esfera
def interseccion_esfera(centro, radio, origen_rayo, direccion_rayo):
    b = 2 * np.dot(direccion_rayo, origen_rayo - centro)
    c = np.linalg.norm(origen_rayo - centro) ** 2 - radio ** 2
    # Calculo de discriminante
    delta = b ** 2 - 4 * c
    if delta > 0:
        # Calculo de los puntos de inteseccion
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            # Retornamos el que se encuentra mas cerca
            return min(t1, t2)
    return None

# Funcion del objeto mas cercano intersectado
def objeto_intersectado_mas_cercano(objetos, origen_rayo, direccion_rayo):
    distancias = [interseccion_esfera(obj['centro'], obj['radio'], origen_rayo, direccion_rayo) for obj in objetos]
    objeto_mas_cercano = None
    distancia_minima = np.inf
    for indice, distancia in enumerate(distancias):
        if distancia and distancia < distancia_minima:
            distancia_minima = distancia
            objeto_mas_cercano = objetos[indice]
    return objeto_mas_cercano, distancia_minima

# Definios la dimensiones de la pantalla
ancho = 300
altura = 160

profundidad_maxima = 3

# Ubicacion de la camara
camara = np.array([0, 0, 1])
ratio = float(ancho) / altura
pantalla = (-1, 1 / ratio, 1, -1 / ratio) # izquierda, arriba, derecha, abajo

# Ubicacion la fuente de luz
luz = { 'posicion': np.array([-0.5, 1.5, -0.2]), 'ambiente': np.array([1, 1, 1]), 'difuso': np.array([1, 1, 1]), 'especular': np.array([1, 1, 1]) }

# Definicion de los objetos
objetos = [
{ 'centro': np.array([1.1, 0.3, -1.5]), 'radio': 0.8, 'ambiente': np.array([0.1, 0, 0]), 'difuso': np.array([0.7, 0, 0]), 'especular': np.array([0.7, 0.7, 0.7]), 'brillo': 80,'reflexion': 0.4 },
{ 'centro': np.array([-0.1, -0.2, -1.3]), 'radio': 0.45, 'ambiente': np.array([0.1, 0.1, 0.1]), 'difuso': np.array([0.7, 0.7, 0.7]), 'especular': np.array([0.7, 0.7, 0.7]), 'brillo': 100, 'reflexion': 0.2 },
{ 'centro': np.array([1.7, -0.3, -0.8]), 'radio': 0.3, 'ambiente': np.array([0, 0.1, 0]), 'difuso': np.array([0, 0.6, 0]), 'especular': np.array([0.7, 0.7, 0.7]), 'brillo': 100, 'reflexion': 0.4 },
{ 'centro': np.array([0.7, -0.5, -0.8]), 'radio': 0.25, 'ambiente': np.array([0, 0, 0.1]), 'difuso': np.array([0.5, 0.2, 0.9]), 'especular': np.array([0.7, 0.7, 0.7]), 'brillo': 100, 'reflexion': 0.2 },
{ 'centro': np.array([-1.3, -0.2, -1]), 'radio': 0.4, 'ambiente': np.array([0, 0, 0.1]), 'difuso': np.array([0.3, 0.3, 1]), 'especular': np.array([0.7, 0.7, 0.7]), 'brillo': 100, 'reflexion': 0.1 },
{ 'centro': np.array([-1.9, 0.1, -3]), 'radio': 0.7, 'ambiente': np.array([0, 0, 0.1]), 'difuso': np.array([0.5, 0.2, 0.9]), 'especular': np.array([0.7, 0.7, 0.7]), 'brillo': 100, 'reflexion': 0.2 },
{ 'centro': np.array([-1.3, -0.3, -2]), 'radio': 0.3, 'ambiente': np.array([0.1, 0, 0]), 'difuso': np.array([0.7, 0, 0]), 'especular': np.array([0.7, 0.7, 0.7]), 'brillo': 100, 'reflexion': 0.2 },
{ 'centro': np.array([-0.6, -0.4, -1.8]), 'radio': 0.25, 'ambiente': np.array([0, 0.1, 0]), 'difuso': np.array([0, 0.7, 0]), 'especular': np.array([0.7, 0.7, 0.7]), 'brillo': 100, 'reflexion': 0.2 },
{ 'centro': np.array([0.4, 0, -3]), 'radio': 0.7, 'ambiente': np.array([0, 0, 0.1]), 'difuso': np.array([0, 0, 0.7]), 'especular': np.array([0.7, 0.7, 0.7]), 'brillo': 100, 'reflexion': 0 },
{ 'centro': np.array([0, -9000, 0]), 'radio': 9000 - 0.7, 'ambiente': np.array([0.1, 0.1, 0.1]), 'difuso': np.array([0.6, 0.6, 0.6]), 'especular': np.array([1, 1, 1]), 'brillo': 100, 'reflexion': 0.5 }
]

# Inicializamos una matriz para que almacene los pixeles de la imagen
imagen = np.zeros((altura, ancho, 3))
for i, y in enumerate(np.linspace(pantalla[1], pantalla[3], altura)):
    for j, x in enumerate(np.linspace(pantalla[0], pantalla[2], ancho)):
        # pantalla esta en el origen
        pixel = np.array([x, y, 0])
        origen = camara
        direccion = normalizar(pixel - origen)
        # Definimos los colores para cada pixel
        color = np.zeros((3))
        reflexion = 1

        for k in range(profundidad_maxima):
            # verificar pro intersecciones
            objeto_mas_cercano, distancia_minima = objeto_intersectado_mas_cercano(objetos, origen, direccion)
            if objeto_mas_cercano is None:
                break

            # Calculo de las intersecciones
            interseccion = origen + distancia_minima * direccion
            normal_a_superficie = normalizar(interseccion - objeto_mas_cercano['centro'])
            punto_desplazado = interseccion + 1e-5 * normal_a_superficie   
            interseccion_con_luz = normalizar(luz['posicion'] - punto_desplazado)

            # Calculo de la distancia minima
            _, distancia_minima = objeto_intersectado_mas_cercano(objetos, punto_desplazado, interseccion_con_luz)
            interseccion_con_luz_distancia = np.linalg.norm(luz['posicion'] - interseccion)
            esta_sombreado = distancia_minima < interseccion_con_luz_distancia

            # Verificacion si hay una sombra
            if esta_sombreado:
                break

            # Definimoms la iluminacion
            iluminacion = np.zeros((3))

            # Calculo de la luz ambiental
            iluminacion += objeto_mas_cercano['ambiente'] * luz['ambiente']

            # Calculo de la luz difusa
            iluminacion += objeto_mas_cercano['difuso'] * luz['difuso'] * np.dot(interseccion_con_luz, normal_a_superficie)

            # Calculo de la luz especular
            interseccion_a_camara = normalizar(camara - interseccion)
            H = normalizar(interseccion_con_luz + interseccion_a_camara)
            iluminacion += objeto_mas_cercano['especular'] * luz['especular'] * np.dot(normal_a_superficie, H) ** (objeto_mas_cercano['brillo'] / 4)

            # Calculo de la reflexion
            color += reflexion * iluminacion
            reflexion *= objeto_mas_cercano['reflexion']

            origen = punto_desplazado
            direccion = reflejado(direccion, normal_a_superficie)

        # Generamos la imagen
        imagen[i, j] = np.clip(color, 0, 1)
    
    print("%d/%d" % (i + 1, altura))
# Guargar e imprimir la imagen
plt.imsave('imagen3.png', imagen)
implot = plt.imshow(imagen)
plt.show()