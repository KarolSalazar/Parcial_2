# Parcial de Programacion 2

## Librerías utilizadas

Pandas = pip install pandas
Numpy = pip install numpy
SQLAlchemy = pip install sqlalchemy

#### Opcional

Utilizar el programa DB Browser de SQLite para tener una visual de los datos y las tablas más adecuado

## Puntos a trabajar

1. Construya una clase que pueda recibir como argumentos al momento de definirla el nombre de uno o varios archivos y opcionalmente la ubicación de cada uno. Si no se ingresa la ruta de algun archivo el programa supone que es la ruta actual y lee todos los archivos de datos. Si no se le ingresa el nombre de ningún archivo el programa debe generar la base de datos.

2. Las bases de datos que lee el programa las debe conseguir (O modificar alguna existente dividiéndola en varios archivos) y deben tener varias columnas con el mismo nombre. Al leer las bases de datos se genera una única tabla de datos con las columnas comunes y los datos de todos los archivos. La tabla final no puede tener filas que tengan en común más de tres valores (Solo se dejaría uno de ellos por considerarse datos repetidos)

3. Grafique el resultado de una regresión líneal. En scatter los valores de la tabla y en línea la regresión lineal.

4. Realice un método o una función que al recibir una función matemática definida a partir de una lambda, realice su integral, su derivada y las grafique.

5. Defina y use al menos dos decoradores

6. Use \*args y \*\*kwargs

7. Documente TODAS las funciones y métodos
