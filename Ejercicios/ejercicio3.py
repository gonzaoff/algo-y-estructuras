import os
os.system("cls")

def promAlt():
    cantEst=int(input("Cuantos estudiantes son: "))
    estudiantes = [float() for i in range(cantEst)]

    for altura in range(cantEst):
        datos=float(input("Ingrese la altura de los estudiantes: "))
        estudiantes[altura]=datos

    for altura in range(cantEst):
        sumaAltura=float()
        sumaAltura += estudiantes[altura]
        promedioAltura = sumaAltura / cantEst
    print(f"El promedio de altura es: {promedioAltura}")
    
    
    
    
def promAlt2():
    cant_est = int(input("Cuántos estudiantes son: "))

    alturas = [float() for i in range(cant_est)]
    for i in range(cant_est):
        altura = float(input(f"Ingrese la altura del estudiante {i+1}: "))
        alturas[i] = altura

    suma_alturas = 0.0 
    for i in range(cant_est):
        suma_alturas += alturas[i]

    promedio_altura = suma_alturas / cant_est

    print(f"El promedio de altura es: {promedio_altura}")

# promAlt2()

print("Hola")

def productosEmpresas():
    
    tamaño=10
    
    vectorA=[int() for i in range(10)]
    vectorB=[int() for i in range(10)]
    vectorC=[int() for i in range(10)]
    
    for i in range(tamaño):
        vectorA=int(input("Ingrese valor de las existencias: "))
        vectorB=int(input("Ingrese valor de los pedidos: "))
        
    for i in range(tamaño):
        if vectorA[i] == vectorB[i]:
            vectorC[i] = vectorA[i]
    
        elif vectorB[i] > vectorA[i]:
            diferencia = vectorB[i] - vectorA[i]
            vectorC[i] = 2 * diferencia
            
        else:
            vectorC[i] = vectorB[i]
            
    print("Vector C: ")
    for valor in vectorC:
        print(valor)

# productosEmpresas()

def encontrar_combinacion(valores, objetivo):
    combinaciones = []
    encontrar_combinacion_recursiva(valores, objetivo, [], combinaciones)
    return combinaciones

def encontrar_combinacion_recursiva(valores, objetivo, combinacion_actual, combinaciones):
    suma_actual = sum(combinacion_actual)
    
    if suma_actual == objetivo:
        combinaciones.append(combinacion_actual[:])
    elif suma_actual < objetivo:
        for i in range(len(valores)):
            nuevo_objetivo = objetivo - suma_actual
            nuevo_valores = valores[i+1:]
            nueva_combinacion = combinacion_actual + [valores[i]]
            encontrar_combinacion_recursiva(nuevo_valores, nuevo_objetivo, nueva_combinacion, combinaciones)

# Ejemplo de uso
valores = [2, 4, 6, 8, 10]
objetivo = 12

combinaciones = encontrar_combinacion(valores, objetivo)
for combinacion in combinaciones:
    print(combinacion)
