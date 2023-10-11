def verificarMultiplo(numero1,comparativa1,numero2,comparativa2,numero3,comparativa3,numero4,comparativa4,numero5,comparativa5):
    #input: cinco numeros y si es multiplo de 3 o 5
    #output: valor booleano indicando si es multiplo o no

    if numero1%comparativa1==0:
        print(True)
    else:
        print(False)

    if numero2%comparativa2==0:
        print(True)

    if numero3%comparativa3==0:
        print(True)
    else:
        print(False)

    if numero4%comparativa4==0:
        print(True)
    else:
        print(False)

    if numero5%comparativa5==0:
        print(True)
    else:
        print(False)

verificarMultiplo(3,5,1,5,3,3,65,5,18,3)



    