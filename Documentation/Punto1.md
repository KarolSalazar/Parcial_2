# Punto1.py

Este archivo contiene la clase Ejercicio1, donde realizaremos la lectura de rutas y seleccionaremos diferentes tipos de archivos

También tenemos las siguientes importaciones:

## Importaciones

```python
import os
import pandas as pd
```

Aquí hacemos uso de 2 librerías diferentes:

1. os: esta librería nos permite utilizar el manejo de archivos

2. pandas: esta librería la utilizamos para la lectura de los datasets o archivos .csv

## init

Aquí hacemos la inicialización de la clase Ejercicio1, de la siguiente manera:

```python
if archivo_path is None or archivo_path=="":
    self.archivo_path = os.getcwd()
else:
    self.archivo_path = archivo_path
    if not os.path.exists(archivo_path):
        raise ValueError(f"No existe la ruta proporcionada '{archivo_path}' ")
```

Aquí lo que hacemos es verificar que si existe o no el path el archivo realizamos acciones diferentes. En caso de que no se haya ingresado ninguna ruta se utilizará la ruta actual. En caso de que se haya ingresado una ruta se verifica si existe o no existe, y en caso de no existir arroja un error

## choose_archivo

Esta función nos permite escoger los archivos que están dentro de la Ruta a trabajar, así:

```python
archivos = os.listdir(self.archivo_path)
csv_archivos = [f for f in archivos if f.endswith('.csv')]
if not csv_archivos:
    print("No se encontraron archivos CSV en la ruta especificada, generando base de datos")
    self.db = self.generate_database()
    self.db.to_csv(self.archivo_path + "\\baseDatos.csv")
    return self.choose_archivo()
print("Archivos CSV encontrados: \n")
for i, archivo in enumerate(csv_archivos):
    print(f"{i+1}. {archivo}")
archivo_indexes = input("\n Selecciona que archivos deseas abrir separados por punto y coma: ").split(";")
selected_archivos = []
for index in archivo_indexes:
    archivo_index = int(index) - 1
    if archivo_index < 0 or archivo_index >= len(csv_archivos):
        raise ValueError("Índice de archivo inválido")
    selected_archivos.append(os.path.join(self.archivo_path, csv_archivos[archivo_index]))
return selected_archivos
```

Aquí lo que hacemos es que crearemos una lista de los archivos de extensión ".csv" en caso de no encontrarse entonces generaremos un archivo, una vez hecho esto volverá a llamar al método para reconocer la lista de archivos.

En caso de haberlos encontrado nos listará los diferentes archivos que hay, posteriormente se le preguntará al usuario los archivos que desea abrir separándolos por punto y coma ";". Después se le mostrará al usuario el contenido de estos archivos, es importante tener en cuenta de que si no hay archivos o se coloca una entrada inválida se lanzará un error

## lector_csv_archivos

Esta función lo que hace es leer el contenido csv de los archivos, así:

```python
csv_archivos = self.choose_archivo()

list_data = []
for csv_archivo in csv_archivos:
    data = pd.read_csv(csv_archivo)
    list_data.append(data)
return list_data
```

Aquí lo que hacemos es crear una lista donde estará almacenada la Data del archivo, posteriormente recorreremos el archivo csv y tomaremos la data que haya dentro de este (esto depende de la cantidad de archivos que hayamos ingresado), es decir, que toma la data del archivo y la añade a la lista

## generate_database

Este método lo utilizamos para generar la base de datos en caso de que no exista:

```python
data = {'id': [1005, 2005, 3005, 4005, 5005],
    'nombre': ['Pablito', 'Clavó', 'Un clavito', 'Calvito', 'Manzana'],
    'edad': [25, 30, 27, 23, 28]}
print(data)
return pd.DataFrame(data)
```

Es un método sencillo en el cuál creamos un dataframe con datos básicos que se utilizará para generar la base de datos.
