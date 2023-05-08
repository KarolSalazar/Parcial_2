# Punto12.py

Dentro de este archivo están las diferentes funciones que se necesitan para que podamos graficar los datos de una función Líneal, aquí se utilizan algunos fundamentos de Inteligencia artificial, para que el programa no sólo sea capaz de generar una regresión lineal, sino también sea capaz de predecir algunos datos, este consta de diferentes funciones que iremos explicando.

También tenemos las siguientes importaciones:

## Importaciones

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
```

Aquí hacemos uso de 3 librerías diferentes:

1. pandas: esta librería la utilizamos para la lectura de los datasets o archivos .csv

2. matplotlib: esta librería la utilizamos para realizar las funciones de graficado

3. scikit_learn: de esta amplia librería tomamos la encargada de regresión lineal que nos sirve para la predicción de datos

## init

Esta clase es la encargada de inicializar o generar la instancia de la clase Ejercicio12, este consta de dos partes:

1. Definición de los datasets a utilizar

```python
self.dataset = pd.read_csv("Regresion\entrenamiento.csv")
self.dataset1 = pd.read_csv("Regresion\prueba.csv")
```

Nótese que estos datasets ya vienen predefinidos dentro de una carpeta llamada regresion

2. Verificacion de que no haya valores vacíos o que ciertos valores estén "null"

```python
self.dataset = self.dataset.dropna()
self.dataset1 = self.dataset1.dropna()
```

El método dropna lo que hace es que retira del dataset esos datos que pueden llegar a ser algo estorbosos, o en su defecto que en caso de ser nulos los retire para evitar inconvenientes

## definir_variables

Dentro de este método definimos las variables _X_ y _Y_ que vamos a utilizar para entrenar y probar los resultados, para definir estas variables, hacemos los siguiente:

```python
self.X_train = self.dataset.iloc[:, :-1].values
self.y_train = self.dataset.iloc[:, 1].values
self.X_test = self.dataset1.iloc[:, :-1].values
self.y_test = self.dataset1.iloc[:, 1].values
```

El método "iloc" lo que hace es que nos ayuda a que podamos obener el valor de la columna que necesitamos del dataset, como nuestros datasets sólo tienen 2 columnas lo hacemos de la manera como se muestra dentro del bloque de código

## definir_regresiones

Este método lo que nos permite es utilizar los métodos de regresión linear dentro de las librerías de sickit_learn:

```python
self.regressor = LinearRegression()
self.regressor.fit(self.X_train, self.y_train)
self.y_pred = self.regressor.predict(self.X_test)
```

Dentro de "fit" lo que hacemos es utilizar los datos de entrenamiento de nuestro dataset que ya habíamos definido,y utilizamos una variable y_pred, para que a partir de los datos obtenidos en el set de entrenamiento, sea capaz de predecir los datos según lo que haya en el archivo test. En otras palabras, tomamos los datos del archivo train, para que nuestra "IA" sea capaz de a partir de esos datos predecir unos nuevos

## graficar_set_prueba, graficar_set_entrenamiento

Estos dos métodos son muy similares, ya que ambos cumplen la misma funcion, sin embargo uno se utilizará para el set de entrenamiento y el otro para el set de prueba, de la siguiente forma:

```python
# visualización para el set de prueba
plt.scatter(self.X_test, self.y_test, color="red")
plt.plot(self.X_train, self.regressor.predict(
    self.X_train), color="blue")
plt.title('Linear Regression (Set de Prueba)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
```

En la primera línea definimos los ejes, y los puntos de intersección y los pintamos de color rojo, después lo que hacemos es tomar los datos que habrán dentro de X y Y, en este caso para el de prueba, nuestro eje X será el que definimos, y el Y será el que se utilizó para predecir los datos, será definido con una línea azul. Por último añadimos el título a la gráfica, luego el nombre de los ejes, y se muestra el gráfico.

Cabe resaltar que para el set de entrenamiento es muy similar, solo que en vez de utilizar un predict, utilizamos los ejes de X_train y y_train.
