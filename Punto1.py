import os
import pandas as pd

class Ejercicio1:
    """
    Esta clase resuelve todo lo relacionado al ejercicio 1 del parcial de programación
    """

    def __init__(self, archivo_path=None):
        if archivo_path is None or archivo_path=="":
            self.archivo_path = os.getcwd()  # Si no se proporciona una ruta, usar la ruta actual
        else:
            self.archivo_path = archivo_path
            if not os.path.exists(archivo_path):
                raise ValueError(f"No existe la ruta proporcionada '{archivo_path}' ")

    def archivo_path(self):
        archivo_path = input("\n Ingresa la ruta del archivo o presiona Enter para usar la ruta actual:\n")
        if archivo_path == "":
            self.archivo_path = os.getcwd()
        else:
            self.archivo_path = archivo_path
            if not os.path.exists(archivo_path):
                raise ValueError(f"No existe la ruta proporcionada '{archivo_path}' ")
        self.db = None

    def choose_archivo(self):
        archivos = os.listdir(self.archivo_path)
        csv_archivos = [f for f in archivos if f.endswith('.csv')]
        if not csv_archivos:
            print("No se encontraron archivos CSV en la ruta especificada, generando base de datos")
            self.db = self.generate_database()
            self.db.to_csv(self.archivo_path + "\\baseDatos.csv")
        print("Archivos CSV encontrados: \n")
        for i, archivo in enumerate(csv_archivos):
            print(f"{i+1}. {archivo}")
        archivo_indexes = input("\n Selecciona que archivos deseas abrir separados por espacio: ").split(" ")
        selected_archivos = []
        for index in archivo_indexes:
            archivo_index = int(index) - 1
            if archivo_index < 0 or archivo_index >= len(csv_archivos):
                raise ValueError("Índice de archivo inválido")
            selected_archivos.append(os.path.join(self.archivo_path, csv_archivos[archivo_index]))
        return selected_archivos

    def lector_csv_archivos(self):
        csv_archivos = self.choose_archivo()
    
        list_data = []
        for csv_archivo in csv_archivos:
            data = pd.read_csv(csv_archivo)
            list_data.append(data)
        return list_data
    
    def generate_database(self):
    # Función que genera una nueva base de datos

    # Se crea un dataframe de ejemplo
        data = {'id': [1005, 2005, 3005, 4005, 5005],
            'nombre': ['Pablito', 'Clavó', 'Un clavito', 'Calvito', 'Manzana'],
            'edad': [25, 30, 27, 23, 28]}
        print(data)
        return pd.DataFrame(data)
    

csv_lector = Ejercicio1()
csv_lector.archivo_path() 
data = csv_lector.lector_csv_archivos()
print(data)