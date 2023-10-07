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

def Notas():  # sourcery skip: convert-to-enumerate, move-assign-in-block
    
#estado:
    promocionados=0
    regularizados=0
    reprobados=0
    
#indice:
    iAlu = 0
    iNota=0
    iMay=0
    rp=0
    rg=0
    p=0
    
#otras:
    notaMayor=0
    mejorAlumno=str()
    suma=0

#Inicio:

    cantAlumn=int(input("Cuantos alumnos son: "))

    alumnos = [str() for i in range(cantAlumn)]
    notas = [int() for i in range(cantAlumn)]

    # recorremos el arreglo "alumnos" y agregamos los strings.
    for i in range(cantAlumn):
        alumno = input("\nIngrese nombre del alumno: ")
        alumnos[iAlu] = alumno
        iAlu += 1
    
    # recorremos el arreglo "notas" y agregamos los floats.
    for j in range(cantAlumn):
            
        nota = float(input(f"\nIngrese un valor del 0 al 10 para la notas de {alumnos[j]}: "))
        notas[iNota] = nota
        iNota += 1
        
        #Si la variable "nota" posee un valor mayor al valor de "notaMayor"
        if nota > notaMayor:
            notaMayor = nota
            iMay = j
            mejorAlumno = alumnos[iMay]
        
        #Si la varible "nota" posee un valor menor o igual a 5 se agrega un valor al arreglo "reprobados".
        if nota <= 5:
            reprobados += 1
            
            nombreReprobados = [str() for i in range(reprobados)]
            nombreReprobados[rp] = alumnos[j]
            
            notaReprobados=[float() for i in range(reprobados)]
            notaReprobados[rp] = nota

            rp += 1
        
        #Si la varible "nota" posee un valor mayor o igual 5 y menor a 7 se agrega un valor al arreglo "regularizados".
        elif nota >= 5 and nota <= 6:
            regularizados += 1

            nombreRegularizados = [str() for i in range(regularizados)]
            nombreRegularizados[rg] = alumnos[j]
            
            notaRegularizados=[float() for i in range(regularizados)]
            notaRegularizados[rg] = nota

            rg += 1
            
        #Si la nota es mayor a 7 se agrega un valor al arreglo "promocionados".
        elif nota >= 7:
            promocionados += 1
            
            nombrePromocionados = [str() for i in range(promocionados)]
            nombrePromocionados[p] = alumnos[j]
            
            notaPromocionados=[float() for i in range(promocionados)]
            notaPromocionados[p] = nota

            p += 1
    
    #Suma las cantidades dentro del array "notas" y las almacena en la variable "suma", luego realiza su promedio
    for i in range(cantAlumn):
        suma += float(notas[i]) 
        promedioNotas = suma / cantAlumn
    
    print(f"""-------------------------------
Cantidad de promocionados: {promocionados}
Cantidad de regularizados: {regularizados}
Cantidad de reprobados: {reprobados}
Promedio general de la clase: {promedioNotas}
Mejor alumno: {mejorAlumno} con {notaMayor}
-------------------------------\n""")
    
# Notas()

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

productosEmpresas()