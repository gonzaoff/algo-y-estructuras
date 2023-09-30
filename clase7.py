# temperatura=[0,0,0,0,0,0,0,0]
# temperatura[0]=100
# temperatura[7]=100
# temperatura[5]=100

# print(temperatura)

# for i in range(7):
#     nueva=temperatura[i]+50
#     print(nueva)


# sourcery skip: for-index-underscore

def val():   # sourcery skip: for-index-underscore, move-assign-in-block, sum-comprehension
    
    cantidad=int(input("cuantos valores agregara?: "))
    valores=[int for i in range(cantidad)]
    resultado = int()
    promedio= int()
    mayor= int()

    for temperaturas in range(cantidad):

        valores[temperaturas]=int(input("Agregar temperaturas: "))
        resultado=resultado+valores[temperaturas]

    promedio=resultado/cantidad


    for valor in valores:
        if valor >= promedio:
            mayor += 1
    print(mayor)
    print(promedio)

# val()

def val2():
    cantidad = int(input("cuantos valores agregara?: "))
    valores = [int(input("Agregar temperaturas: ")) for _ in range(cantidad)]
    resultado = sum(valores)
    promedio = resultado / cantidad
    mayor = 0

    for valor in valores:
        if valor >= promedio:
            mayor += 1

    print(mayor)
    print(promedio)

# val2()

def nombress():  # sourcery skip: for-index-underscore
    #input: el nombre
    #output: si el nombre es true en la lista
    n = int(input("ingrese la cantidad: "))
    nombres= [str for i in range(n)]
    for i in range(n):
        nombres[i]=input("ingrese el nombre: ")
    
    buscado = input("Ingrese el nombre a buscar: ")
    encontrado = False
    
    for i in range(n):
        if nombres[i] == buscado:
            encontrado = True
    
    if encontrado:
        print("se encontro.")
    else:
        print("no se encontro")
    
nombress()




