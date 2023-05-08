# Parcial de Programacion 2

Antes de empezar con la documentación cabe aclarar que se prefirió trabajar los puntos por separado, ya que aunque se menciona trabajar una clase conjuta, por cuestiones de buenas prácticas y de orden para una mejor claridad en los ejercicios, se decidió colocar cada ejercicio de manera individual. Por lo que dentro de la carpeta scripts esejecutar individualmente cada ejercicio

## Librerías utilizadas

Pandas = pip install pandas
Numpy = pip install numpy
SQLAlchemy = pip install sqlalchemy
pip install SQLAlchemy Flask-SQLAlchemy (Es necesario ejecutar ambas)
Matplotlib = pip install matplotlib
Scikit-learn = pip install scikit-learn

#### Opcional

Utilizar el programa DB Browser de SQLite para tener una visual de los datos y las tablas más adecuado

## Explicación Archivos

### Archivos Python

La explicación de estos archivos está dentro de la carpeta Documentation para poder explicar más a fondo archivo por archivo

### Otros archivos

Dentro de la carpeta Database, tenemos tanto el modelo con las conexiones de la base de datos, adicionalmente se incluye un archivo "BaseDatosParcial2.sql" donde al ejecutarse se crea nuestra base de datos (en caso de ser necesario), CreacionTablas.sql sólo crea las tablas, e InsercionTablas.sql sólo inserta los datos dentro de las tablas, el archivo con extensión .sqlite es la base de datos ya creada. Y la imagen muestra el esquema que tienen las tablas.

El archivo .gitignore tiene la carpeta que genera visual studio ya que contiene archivos innecesarios, contiene la base de datos que genera el propio programa y un archivo .\*-journal que a veces se genera al trabajar en la base de datos SQLite

## Puntos a trabajar

1. Construya una clase que pueda recibir como argumentos al momento de definirla el nombre de uno o varios archivos y opcionalmente la ubicación de cada uno. Si no se ingresa la ruta de algun archivo el programa supone que es la ruta actual y lee todos los archivos de datos. Si no se le ingresa el nombre de ningún archivo el programa debe generar la base de datos.

2. Las bases de datos que lee el programa las debe conseguir (O modificar alguna existente dividiéndola en varios archivos) y deben tener varias columnas con el mismo nombre. Al leer las bases de datos se genera una única tabla de datos con las columnas comunes y los datos de todos los archivos. La tabla final no puede tener filas que tengan en común más de tres valores (Solo se dejaría uno de ellos por considerarse datos repetidos)

3. Grafique el resultado de una regresión líneal. En scatter los valores de la tabla y en línea la regresión lineal.

4. Realice un método o una función que al recibir una función matemática definida a partir de una lambda, realice su integral, su derivada y las grafique.

5. Defina y use al menos dos decoradores

6. Use \*args y \*\*kwargs

7. Documente TODAS las funciones y métodos
