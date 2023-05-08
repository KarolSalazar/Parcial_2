# Punto13.py

Este archivo contiene la clase Ejercicio13, donde vamos a derivar e integrar una función y hacer sus respectivas gráficas. Pueden presentarse ciertas limitantes a la hora de probar ciertas funciones, ya que no siempre un método de derivación y/o integración funciona para todo tipo de funciones

También tenemos las siguientes importaciones:

## Importaciones

```python
import numpy as np
import matplotlib.pyplot as plt
```

Aquí hacemos uso de 2 librerías diferentes:

1. numpy: librería que nos permite trabajar ciertas funciones matemáticas

2. matplotlib: librería que nos permite graficar funciones en python

## init

En esta función inicializamos el ejercicio13:

```python
self.a = a
self.b = b
self.x = np.linspace(self.a, self.b, 10000)
# Esta es la función a cambiar
self.func = np.sin(self.x)
# Evaluar la función en el rango de valores x
self.y = self.func
```

Aquí creamos los valores que necesitaremos de a y b, y el rango de valores que trabajaremos en X (de a, hasta b), además de la función con la que vamos a trabajar sin(x). Esta función la podemos cambiar por otras por ejemplo sin(x)+cos(x)

```python
self.func = np.sin(self.x)+np.cos(self.x)
```

## calcular_integral

En esta función realizamos el cálculo de la integral, dónde recorremos el rango de valores de x

```python
integral = np.zeros_like(self.x)
for i in range(len(self.x)):
    integral[i] = np.trapz(self.y[:i+1], self.x[:i+1])

return integral
```

Aquí se inicializa la integral y posteriormente procedemos a recorrer la función que tenemos en el rango de valores que hemos tomado en X y en Y

## calcular derivada

Esta función nos ayuda a calcular la derivada de la función

```python
derivada = np.gradient(self.y, self.x)
return derivada
```

Como podemos observar para este caso utilizamos la gradiente que nos resulta más sencillo de trabajar

## graficar

Aquí en resumidas palabras estamos utilizando matplotlib para graficar las funciones

```python

# Graficar la función original
plt.subplot(2, 1, 1)
plt.plot(self.x, self.y)
plt.grid(True)
plt.title('Función Original')

# Graficar la integral de la función
plt.subplot(2, 2, 3)
plt.plot(self.x, self.y, label='Área bajo la curva')
plt.plot(self.x, integral, label='Antiderivada')
plt.fill_between(self.x, self.y, alpha=0.3)  # Rellenar eárea bajo la curva de la función
plt.legend()
plt.grid(True)

# Graficar la derivada de la función
plt.subplot(2,2,4)
plt.plot(self.x,self.y, label="Función")
plt.plot(self.x, derivada, color="deeppink"label="Derivada")
plt.legend(loc = "best")
plt.grid(True)
plt.title('Derivada')

# Mostrar las gráficas
#plt.tight_layout()
plt.show()

```

Cuando llamamos a Plor lo que hacemos es generar la gráfica, posteriormente se decora, y se rellena según las necesidades para la gráfica original, la derivada y la antiderivada.
