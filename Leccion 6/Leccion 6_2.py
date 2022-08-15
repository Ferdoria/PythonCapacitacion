# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que
# tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def datos(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def calificacion(self):
        if self.nota >= 2:
            print("Aprobado")
        else:
            print("No aprobado")

alumno= Alumno()
alumno.datos("Fernando", 3)
alumno.imprimir()
alumno.calificacion()