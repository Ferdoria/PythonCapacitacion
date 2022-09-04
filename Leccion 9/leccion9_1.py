# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
# paraguay, bolivia, brasil, argentina, bolivia, paraguay, uruguay, brasil
datos = input("ingresar Paises separados por comas:\n")
listaPais = []
for item in datos.split(","):
    if item.strip() not in listaPais:
        listaPais.append(item.strip())

print("lista sin duplicados:", listaPais)
listaPais = sorted(listaPais)
print("lista Ordenada:", listaPais)


