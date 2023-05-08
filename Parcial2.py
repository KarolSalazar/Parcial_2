from scripts.Punto1 import *
from scripts.Punto2 import *
from scripts.Punto12 import *
from scripts.Punto13 import *

import math


class Parcial2:
    def __init__(self):
        pass

    def ejecutar_punto_1(self):
        csv_lector = Ejercicio1()
        csv_lector.archivo_path()
        data = csv_lector.lector_csv_archivos()
        print(data)

    def ejecutar_punto_2(self):
        lector_tablas = Ejercicio2()
        lector_tablas.consulta_sql()

    def ejecutar_punto_12(self):
        graficador = Ejercicio12()
        graficador.definir_variables()
        graficador.definir_regresion()
        graficador.graficar_set_entrenamiento()
        graficador.graficar_set_prueba()

    def ejecutar_punto_13(self):
        a = 0
        b = 15
        graficador = Ejercicio13(a, b)
        integral = graficador.calcular_integral()
        derivada = graficador.calcular_derivada()
        graficador.graficar(integral, derivada)
