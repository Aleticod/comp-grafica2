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
x = [0.90, 1.30, 1.90, 2.10, 2.60, 3.00, 3.90, 4.40, 4.70, 5.00, 6.00, 7.00, 8.00, 9.20, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3]
y = [1.30, 1.50, 1.85, 2.10, 2.60, 2.70, 2.40, 2.15, 2.05, 2.10, 2.25, 2.30, 2.25, 1.95, 1.40, 0.90, 0.70, 0.60, 0.50, 0.40, 0.25]

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

# Configuración de la leyenda y guardar la figura
plt.legend()
#plt.savefig('spline.png')
plt.show()
