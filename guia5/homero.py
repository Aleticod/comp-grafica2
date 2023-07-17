import matplotlib.pyplot as plt
import numpy as np

def spline(x, y):
    n = len(x)
    a = {k: v for k, v in enumerate(y)}
    h = {k: x[k+1] - x[k] for k in range(n - 1)}
    
    # Creación de la matriz A
    A = [[1] + [0] * (n - 1)]
    for i in range(1, n-1):
        row = [0] * n
        row[i - 1] = h[i - 1]
        row[i] = 2*(h[i-1] + h[i])
        row[i+1] = h[i]
        A.append(row)
    A.append([0] * (n-1) + [1])
    
    # Creación del vector B
    B = [0]
    for k in range(1, n-1):
        row = 3 * (a[k+1] - a[k]) / h[k] - 3 * (a[k] - a[k-1])/h[k-1]
        B.append(row)
    B.append(0)
    
    # Resolución del sistema lineal A*c = B
    c = dict(zip(range(n), np.linalg.solve(A, B)))
    
    # Cálculo de los coeficientes b y d
    b = {}
    d = {}
    for k in range(n-1):
        b[k] = (1/h[k]) * (a[k+1] - a[k]) - (h[k]/3) * (2*c[k] + c[k+1])
        d[k] = (c[k+1] - c[k]) / (3*h[k])
    
    # Creación de las ecuaciones de los segmentos y sus dominios
    s = {}
    for k in range(n-1):
        eq = f'{a[k]}{b[k]:+}*(x-{x[k]}){c[k]:+}*(x-{x[k]})**2{d[k]:+}*(x-{x[k]})**3'
        s[k] = {'eq': eq, 'domain': [x[k], x[k+1]]}
    
    return s

# Datos de ejemplo
x = [2.86, 2.91, 2.99, 3.18, 3.38, 3.59, 3.79, 4.23, 4.46, 4.69, 5.15, 5.40, 5.66, 5.88, 6.07, 6.25, 6.40, 6.50, 6.61, 6.71, 6.80, 6.87, 6.92, 6.99, 7.02, 7.04, 7.05]
y = [7.51, 7.81, 8.06, 8.44, 8.69, 8.85, 8.98, 9.17, 9.23, 9.27, 9.29, 9.27, 9.21, 9.16, 9.08, 8.98, 8.88, 8.78, 8.67, 8.55, 8.40, 8.27, 8.14, 7.96, 7.77, 7.65, 7.55] 

# Cálculo de las ecuaciones de los segmentos cúbicos
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")

# Graficar los puntos de datos
plt.scatter(x, y)

x = [7.05, 7.10, 7.18, 7.26, 7.30, 7.32]
y = [7.55, 7.53, 7.49, 7.39, 7.28, 7.20]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [7.32, 7.31, 7.29, 7.27, 7.22]
y = [7.20, 7.14, 7.09, 7.04, 6.97]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [5.80, 5.95, 6.15, 6.37, 6.55, 6.77, 6.92, 7.09, 7.22, 7.37, 7.42, 7.47, 7.48]
y = [6.80, 6.96, 7.09, 7.16, 7.19, 7.17, 7.12, 7.05, 6.97, 6.78, 6.68, 6.56, 6.43]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [3.94, 3.96, 4.04, 4.16, 4.36, 4.58, 4.84, 5.10, 5.28, 5.46, 5.64, 5.80, 5.88, 5.95, 5.98]
y = [6.33, 6.46, 6.65, 6.81, 6.99, 7.11, 7.17, 7.18, 7.14, 7.08, 6.95, 6.80, 6.67, 6.49, 6.33]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [3.94, 3.96, 4.00, 4.08, 4.18, 4.32, 4.49, 4.68, 4.89, 5.10, 5.30, 5.46, 5.63, 5.75, 5.85, 5.94, 5.98]
y = [6.33, 6.16, 6.00, 5.84, 5.71, 5.58, 5.48, 5.42, 5.39, 5.39, 5.45, 5.52, 5.63, 5.75, 5.89, 6.10, 6.33]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [5.90, 5.98, 6.11, 6.28, 6.43, 6.57, 6.74, 6.88, 6.97, 7.00, 7.03, 7.04]
y = [5.95, 5.96, 5.98, 6.01, 6.04, 6.08, 6.08, 6.01, 5.95, 5.89, 5.81, 5.71]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [7.04, 7.17, 7.24, 7.30, 7.36, 7.40, 7.45, 7.47, 7.48]
y = [5.71, 5.79, 5.86, 5.93, 6.02, 6.10, 6.20, 6.31, 6.43]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [4.11, 4.15, 4.25, 4.39, 4.67, 4.95, 5.28, 5.68, 5.94, 6.26, 6.51, 6.69, 6.84, 6.97, 7.03, 7.04]
y = [4.04, 4.26, 4.51, 4.75, 4.99, 5.13, 5.22, 5.24, 5.21, 5.22, 5.25, 5.31, 5.39, 5.51, 5.63, 5.71]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [6.89, 7.08, 7.23, 7.41, 7.54, 7.72]
y = [5.41, 5.33, 5.26, 5.15, 5.06, 4.90]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [7.16, 7.22, 7.27, 7.29, 7.30]
y = [5.76, 5.69, 5.52, 5.39, 5.24]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [4.11, 4.16, 4.29, 4.50, 4.80, 5.16, 5.50, 5.92, 6.23, 6.58, 6.81, 7.08, 7.23, 7.40]
y = [4.04, 3.70, 3.35, 3.12, 2.91, 2.76, 2.70, 2.74, 2.85, 3.00, 3.16, 3.34, 3.50, 3.72]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [7.23, 7.31, 7.40, 7.52, 7.64, 7.74, 7.84, 7.92, 7.97, 8.00, 8.06, 8.13, 8.22, 8.29]
y = [3.88, 3.78, 3.72, 3.69, 3.69, 3.71, 3.77, 3.88, 4.00, 4.15, 4.26, 4.40, 4.54, 4.75]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [7.60, 7.72, 7.86, 8.00, 8.12, 8.22, 8.27, 8.29]
y = [4.80, 4.90, 4.96, 5.00, 4.98, 4.93, 4.84, 4.75]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [2.86, 2.90, 2.97, 3.07, 3.17, 3.24, 3.32, 3.36]
y = [7.51, 7.17, 6.83, 6.49, 6.17, 5.85, 5.46, 5.10]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [2.95, 3.00, 3.10, 3.24, 3.40, 3.57, 3.74]
y = [4.59, 4.43, 4.32, 4.23, 4.19, 4.20, 4.29]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [2.95, 2.96, 3.01, 3.09, 3.21, 3.39, 3.55, 3.66]
y = [4.59, 4.74, 4.86, 4.95, 5.04, 5.09, 5.04, 4.97]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [3.53, 3.55, 3.57, 3.60]
y = [4.16, 3.91, 3.64, 3.32]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [3.54, 3.57, 3.59, 3.60]
y = [2.72, 2.91, 3.11, 3.32]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [6.54, 6.55, 6.56]
y = [2.93, 2.53, 2.15]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [3.94, 4.05, 4.22, 4.56, 5.00, 5.42, 5.75]
y = [8.66, 9.08, 9.37, 9.60, 9.67, 9.56, 9.26]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [3.35, 3.42, 3.59, 3.87, 4.24, 4.58, 4.91]
y = [8.64, 9.02, 9.33, 9.53, 9.62, 9.57, 9.31]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)

x = [2.86, 2.92, 3.35, 3.62, 3.93]
y = [5.22, 5.54, 5.35, 6.01, 5.30]
eqs = spline(x, y)
print(eqs)

# Graficar los segmentos cúbicos
for key, value in eqs.items():
    def p(x):
        return eval(value['eq'])
    t = np.linspace(*value['domain'], 100)
    plt.plot(t, p(t), label=f"$S_{key}(x)$")
    
# Graficar los puntos de datos
plt.scatter(x, y)


# Configuración de la leyenda y guardar la figura
#plt.legend()
#plt.savefig('spline.png')
plt.show()
