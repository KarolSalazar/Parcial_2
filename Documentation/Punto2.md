# Punto2.py

Este archivo contiene la clase Ejercicio2, donde tomamos valores en común entre tablas, y retiramos los que sean menores a 3 valores repetidos, en este caso sgún el agrupamiento

También tenemos las siguientes importaciones:

## Importaciones

```python
import sqlalchemy
import pandas as pd
```

Aquí hacemos uso de 2 librerías diferentes:

1. sqlalchemy: esta librería nos permite trabajar temas relacionados a SQL desde python (sea SQLite, MySQL, PostgreSQL, etre otros) para este caso usaremos SQLite

2. pandas: esta librería la utilizamos para la lectura de los datasets o archivos .csv

## init

Estemétodo es corto, ya que para inicializar la clase sólo necesitaremos el "engine" o la máquina de base de datos a utilizar

```python
self.dbEngine = self.crear_engine()
```

## crear_engine

Este método es el encargado de generar el engine que estemos utilizando, para este caso SQLite

```python
dbEngine = sqlalchemy.create_engine(
    'sqlite:///Database\BaseDatosParcial2.sqlite')
```

Aquí lo único que hacemos es obtener la base de datos de SQLite que tenemos almacenada

## consulta_sql

Aquí en esta función lo que hacemos es que según la consulta ingresada podamos mostrar la data al usuario:

```python
consulta = input("Ingrese la consulta a realizar:")
if consulta is None or consulta == "" or consulta == "NA":
    consulta = "SELECT l.location_id, l.country_id, l.city, l.state_province, c.country_name, COUNT(*) conteo FROM locations l JOIN countries c ON l.country_id=c.country_id GROUP BY l.country_id HAVING COUNT(*) < 3"
try:
    dataframe = pd.read_sql(consulta, self.dbEngine)
    print("Consulta realizada: ", consulta,
            "\nResultado obtenido: \n", dataframe)
except:
    print("Algo ha salido mal con la consulta, revisa que esté bien redactada, o que la base dedatos si contenga dicha información solicitada")
```

Aquí lo que hacemos es que el usuario tiene la posibilidad de ingresar la consulta, en caso de que no ingrese nada o NA se utilizará una consulta por defecto que se explicará más adelante.

Posteriormente se verifica que la consulta sea correcta, si es correcta, entonces se creará un Dataframe del que se leerá la consulta realizada dentro de nuestra Engine, y se mostrará al usuario dicha información. En caso de que salte error toca verificar si la consulta se hizo correctamente.

## RELACIONADO A SQL

Aquí se explica la consulta que se debe realizar para el ejercicio:

```sqlite
SELECT l.location_id, l.country_id, l.city, l.state_province, c.country_name, COUNT(*) conteo
FROM locations l
JOIN countries c ON l.country_id=c.country_id
GROUP BY l.country_id
HAVING COUNT(*)<3
```

Básicamente aquí tomamos la id de la locación, el código del país, la ciudad, la provincia, el nombre del país y la cantidad de veces que aparece dicho país en la tabla de "locations", lo que hacemos es que tomamos los datos en comun y con el "COUNT(*)" contamos cuantas veces se toma ese país, eso lo hacemos por medio de la llave foránea o ForeignKey del país "country_id" al comparar la llave almacenada en "locations" con la llave primaria de "countries" podemos tener esta cuenta, el *GROUP BY\* nos permite que podamos agrupar las locaciones por país. Normalmente habrían 7 locaciones diferentes, pero al haber agrupado por país y tomado los que se repitan menos de 3 veces, sólo se muestran 3, cabe aclarar además que la columna conteo, nos dice cuantas veces se repite dicho país.

Para comprobar dicha información de que hay varias locaciones se puede ingresar la siguiente consulta:

```sqlite
SELECT * FROM locations
```

Puedes realizar consultas diferentes:

```sqlite
SELECT * FROM employees
```

Esta es para seleccionar los empleados. Y de esta forma tomar otro tipo de datos, pero hay que tener cuidado, ya que si no se hace bien la consulta puede generar error
