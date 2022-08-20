#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

archivo = open('arhivoPrueba.txt', 'w')
archivo.write('Prueba escritura 1 en archivo\n')
archivo.close()

archivo = open('arhivoPrueba.txt', 'r+')
archivo.readline()
archivo.write('prueba escritura 2 en archivo\n')

print(archivo.read())
archivo.close()