import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


class Ejercicio12:
    """
    Esta clase contiene las funciones necesarias para la ejecución del punto 12 
    (Véase el archivo Documentation/Punto12.md)
    """

    def __init__(self):
        self.dataset = pd.read_csv("Regresion\entrenamiento.csv")
        self.dataset1 = pd.read_csv("Regresion\prueba.csv")
        # Validamos que no hayan valores nulos, y en caso de haberlos se corrigen
        self.dataset = self.dataset.dropna()
        self.dataset1 = self.dataset1.dropna()

    def definir_variables(self):
        self.X_train = self.dataset.iloc[:, :-1].values
        self.y_train = self.dataset.iloc[:, 1].values
        self.X_test = self.dataset1.iloc[:, :-1].values
        self.y_test = self.dataset1.iloc[:, 1].values

    def definir_regresion(self):
        self.regressor = LinearRegression()
        self.regressor.fit(self.X_train, self.y_train)
        self.y_pred = self.regressor.predict(self.X_test)

    def graficar_set_entrenamiento(self):
        # visualización para el set de entrenamiento
        plt.scatter(self.X_train, self.y_train, color="red")
        plt.plot(self.X_train, self.regressor.predict(
            self.X_train), color="blue")
        plt.title('Linear Regression (Set de entrenamiento)')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

    def graficar_set_prueba(self):
        # visualización para el set de prueba
        plt.scatter(self.X_test, self.y_test, color="red")
        plt.plot(self.X_train, self.regressor.predict(
            self.X_train), color="blue")
        plt.title('Linear Regression (Set de Prueba)')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()


graficador = Ejercicio12()
graficador.definir_variables()
graficador.definir_regresion()
graficador.graficar_set_entrenamiento()
graficador.graficar_set_prueba()
