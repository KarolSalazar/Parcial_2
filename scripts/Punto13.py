import numpy as np
import matplotlib.pyplot as plt

class Ejercicio13:

    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.x = np.linspace(self.a, self.b, 10000)
        # Esta es la función a cambiar
        self.func = np.sin(self.x)
        # Evaluar la función en el rango de valores x
        self.y = self.func

        # Crear un rango de valores x para evaluar la función
    
    def calcular_integral(self):

    # Calcular la integral de la función, estudiar esta linea
        integral = np.zeros_like(self.x)
        for i in range(len(self.x)):
            integral[i] = np.trapz(self.y[:i+1], self.x[:i+1])

        return integral

    # Calcular la derivada de la función
    def calcular_derivada(self):
        derivada = np.gradient(self.y, self.x)
        return derivada

    def graficar(self, integral, derivada):

        # Graficar la función original
        plt.subplot(2, 1, 1)
        plt.plot(self.x, self.y)
        plt.grid(True)
        plt.title('Función Original')

        # Graficar la integral de la función
        plt.subplot(2, 2, 3)
        plt.plot(self.x, self.y, label='Área bajo la curva')
        plt.plot(self.x, integral, label='Antiderivada')
        plt.fill_between(self.x, self.y, alpha=0.3)  # Rellenar el área bajo la curva de la función
        plt.legend()
        plt.grid(True)

        # Graficar la derivada de la función
        plt.subplot(2,2,4)
        plt.plot(self.x,self.y, label="Función")
        plt.plot(self.x, derivada, color="deeppink", label="Derivada")
        plt.legend(loc = "best")
        plt.grid(True)
        plt.title('Derivada')

        # Mostrar las gráficas
        #plt.tight_layout()
        plt.show()