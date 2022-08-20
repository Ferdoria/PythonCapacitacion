#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

from pickle import *

class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def __str__(self):
        return self.marca + "-" + self.modelo

datos = Vehiculo("Hyundai", "Tucson")
print(datos)

archivo = open('archivoVehiculo.tx', 'w+b')
dump(datos, archivo)

archivo.seek(0)
datos2 = load(archivo)
print(datos2)
archivo.close()

