import sqlalchemy
import pandas as pd


class Ejercicio2:
    """
    Esta clase resuelve todo lo relacionado al ejercicio 2 del parcial de programación
    (Véase el archivo Documentation/Punto2.md)
    """

    def __init__(self):
        self.dbEngine = self.crear_engine()

    def consulta_sql(self):
        consulta = input("Ingrese la consulta a realizar:")
        if consulta is None or consulta == "" or consulta == "NA":
            consulta = "SELECT l.location_id, l.country_id, l.city, l.state_province, c.country_name, COUNT(*) conteo FROM locations l JOIN countries c ON l.country_id=c.country_id GROUP BY l.country_id HAVING COUNT(*) < 3"
        try:
            dataframe = pd.read_sql(consulta, self.dbEngine)
            print("Consulta realizada: ", consulta,
                  "\nResultado obtenido: \n", dataframe)
        except:
            print("Algo ha salido mal con la consulta, revisa que esté bien redactada, o que la base dedatos si contenga dicha información solicitada")

    def crear_engine(self):
        dbEngine = sqlalchemy.create_engine(
            'sqlite:///Database\BaseDatosParcial2.sqlite')

        return dbEngine


consultas = Ejercicio2()
consultas.consulta_sql()
