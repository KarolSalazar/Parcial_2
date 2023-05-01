# Parcial de Programacion 2

## Puntos a trabajar

1. Construya una clase que pueda recibir como argumentos al momento de definirla el nombre de uno o varios archivos y opcionalmente la ubicación de cada uno. Si no se ingresa la ruta de algun archivo el programa supone que es la ruta actual y lee todos los archivos de datos. Si no se le ingresa el nombre de ningún archivo el programa debe generar la base de datos.

2. Las bases de datos que lee el programa las debe conseguir (O modificar alguna existente dividiéndola en varios archivos) y deben tener varias columnas con el mismo nombre. Al leer las bases de datos se genera una única tabla de datos con las columnas comunes y los datos de todos los archivos. La tabla final no puede tener filas que tengan en común más de tres valores (Solo se dejaría uno de ellos por considerarse datos repetidos)

3. La clase debe tener un método que detecte automátiamente en las columnas con valores tipo str los datos que se identifican como diferentes de forma errada por cuestión de tildes o mayúsculas/minúsculas y homogeneizar los valores. Además le debe mostrar al usuario los valores únicos y permitirle decir si desea unir o no algunos de esos valores.

4. La clase debe tener un método que analice la Gausianidad, curtosis y sesgo de cada columna numérica y le dé una gráfica Q-Q de cada columna numérica.

5. La clase debe tener un método que calcule los coeficientes de regresión lineal para dos columnas elegidas por el usuario. (Si hace regresión multi-lineal gana puntos adicionales, si la hace multi-lineal con regularización, gana aún más puntos adicionales)

6. Grafique el resultado del numeral anterior. En scatter los valores de la tabla y en línea la regresión lineal.

7. Realice un método o una función que al recibir una función matemática definida a partir de una lambda, realice su integral, su derivada y las grafique.

8. Defina y use al menos dos decoradores

9. Use \*args y \*\*kwargs

10. Documente TODAS las funciones y métodos
