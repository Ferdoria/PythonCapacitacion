def esPrimo(numero):
    for i in range(2,numero):
        if (numero%i) == 0:
            print ("El numero NO es Primo:", numero)
            break
    else:
        print("El numero es Primo:", numero)

esPrimo(8)