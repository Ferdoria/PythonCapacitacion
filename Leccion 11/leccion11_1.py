# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres
# columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la
# columna apellido que también será de tipo texto.

# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.

# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

conexion = sqlite3.connect("bdleccion11.db")
cursor = conexion.cursor()

# Crear la BD
conexion.execute("""CREATE TABLE Alumnos(
                CodAlum INTEGER PRIMARY KEY AUTOINCREMENT, 
                NomAlum TEXT, 
                ApellAlum TEXT)""")

# Realizar Insert
conexion.execute("INSERT INTO Alumnos(NomAlum, ApellAlum) VALUES(?, ?)", ("Fernando", "Doria"))
conexion.execute("INSERT INTO Alumnos(NomAlum, ApellAlum) VALUES(?, ?)", ("Javier", "Molinas"))
conexion.execute("INSERT INTO Alumnos(NomAlum, ApellAlum) VALUES(?, ?)", ("Lucero", "Morinigo"))
conexion.execute("INSERT INTO Alumnos(NomAlum, ApellAlum) VALUES(?, ?)", ("Daniela", "Doria"))
conexion.execute("INSERT INTO Alumnos(NomAlum, ApellAlum) VALUES(?, ?)", ("Sofia", "Doria"))
conexion.execute("INSERT INTO Alumnos(NomAlum, ApellAlum) VALUES(?, ?)", ("Miguel", "Roman"))
conexion.execute("INSERT INTO Alumnos(NomAlum, ApellAlum) VALUES(?, ?)", ("Angel", "Molinas"))
conexion.execute("INSERT INTO Alumnos(NomAlum, ApellAlum) VALUES(?, ?)", ("Maria", "Memmel"))
conexion.commit()

cursor = conexion.execute("SELECT * FROM Alumnos WHERE NomAlum = 'Angel'")

dato = cursor.fetchall()
print("Alumno es:", dato)

cursor.close()
conexion.close()