def anhoBisiesto(anho):
    if anho % 4 == 0:
        if anho % 100 == 0:
            if anho % 400 == 0:
                print('El año es bisiesto')
            else:
                print('El año no es bisiesto')
        else:
            print('El año es bisiesto.')
    else:
        print('El año no es bisiesto.')
anhoBisiesto(2020)