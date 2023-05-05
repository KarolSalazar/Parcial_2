from Punto1 import *
from Punto2 import *
from Punto13 import *
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

    def ejecutar_punto_13(self):
        a = 0
        b = 15
        func = math.sin()
        graficador = Ejercicio13(func, a, b)
        integral = graficador.calcular_integral()
        derivada = graficador.calcular_derivada()
        graficador.graficar(integral, derivada)
