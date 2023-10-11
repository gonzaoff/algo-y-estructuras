import os
os.system("cls")

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
    #input: la lista de nombres y el nombre a buscar en la lista
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
    
# nombress()


def evaluaciones():
#     //en un curso de 5 estudiantes se toman 3 parciales. diseñar un algoritmo
# //para registrar las notas de los alumnos en una matriz.
# // calcular "promedio de cada alumno" y "promedio de cada parcial"
    matriz=[[float() for parciales in range(3)]for alumnos in range(5)]

    nota = float()
    totalNota=float()
    promedioNota=float()
    
    for alumnos in range(5):
        for parciales in range(3):
            nota=float(input(f"Ingrese la nota del alumno {alumnos+1}: "))
            
    for alumnos in range(5):
        for parciales in range(3):
            totalNota=totalNota+nota
            promedioNota=totalNota/parciales
    
    for alumnos in range(5):
        for parciales in range(3):
            opciones=str(input("Ingrese el alumno de quien se pretende saber las notas y promedios: "))
    
            if opciones == 1:
                print(matriz[parciales])
                opciones=str(input("Ingrese el alumno de quien se pretende saber las notas y promedios: "))
                

    
    
# evaluaciones()

def evaluaciones2():
    # En un curso de 5 estudiantes se toman 3 parciales. Diseñar un algoritmo
    # para registrar las notas de los alumnos en una matriz.
    # Calcular el promedio de cada alumno y el promedio de cada parcial.
    matriz = [[0.0] * 3 for i in range(5)]

    for alumno in range(5):
        for parcial in range(3):
            nota = float(input(f"Ingrese la nota del alumno {alumno+1} en el parcial {parcial+1}: "))
            matriz[alumno][parcial] = nota

    for alumno in range(5):
        suma_notas = 0.0
        for parcial in range(3):
            suma_notas += matriz[alumno][parcial]
        promedio_alumno = suma_notas / 3
        print(f"El promedio del alumno {alumno+1} es: {promedio_alumno}")

    for parcial in range(3):
        suma_notas = 0.0
        for alumno in range(5):
            suma_notas += matriz[alumno][parcial]
        promedio_parcial = suma_notas / 5
        print(f"El promedio del parcial {parcial+1} es: {promedio_parcial}")

evaluaciones2()