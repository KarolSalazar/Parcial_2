import sqlalchemy
import pandas as pd


class Ejercicio2:
    def __init__(self):
        self.dbEngine = self.crear_engine()

    def consulta_sql(self):
        consulta = input("Ingrese la consulta a realizar:")
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
