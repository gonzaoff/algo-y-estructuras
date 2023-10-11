from os import system
system("cls")

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

def choferes():  # sourcery skip: convert-to-enumerate, move-assign-in-block, use-itertools-product

    #indices:
    iKM=0
    iN=0
    iCam=0
    jDia=0
    
    #variables preinicializadas
    suma=0
    diasSemana=7
    mayorKM=0
    kmCh=0
    
    #ingreso la cantidad de choferes
    cantChoferes=int(input("Ingrese la cantidad de choferes: "))
    
    #inicializo las arrays/matrices
    nombres=[str() for i in range(cantChoferes)]
    kilometros = [[0.0] * diasSemana for i in range(cantChoferes)]
    sumaKM=[float() for i in range(cantChoferes)]

    #solicito el nombre del chofer con la variable "nombre" y lo almaceno en la array "nombres" con el indice "iN"
    for i in range(cantChoferes):
        nombre=str(input("\nIngrese el nombre del chofer: "))
        nombres[iN]=nombre
        
        # print(nombres)
        
        #solicito el kilometraje del chofer con la variable "kilometro" y lo almaceno en la array "kilometros" con los indices "[i][j]"
        for j in range(diasSemana):
            kilometro=float(input(f"\ningrese los km recorridos el dia {j+1}: "))
            kilometros[i][j] = kilometro
            
            # si la variable "kilometro" es mayor a "mayorKM" entonces almaceno el valor de "kilometro" en "mayorKM",  
            # el indice del nombre del chofer "i" en "iCam", guardo su valor en "mejorCh", y el dia "j+1" en "jDia"
            if kilometro > mayorKM:
                mayorKM = kilometro
                iCam = i
                jDia = j+1
                mejorCh = nombres[iCam]
        # print(kilometros)
        
        iN+=1
        
        #Sumo los valores de "i"(diasSemana) para cada "j"(cantChoferes) y lo almaceno en la array "sumaKM" con su indice
        # de esta forma determino la suma de km para cada chofer ##Sin uso
        for i in range(diasSemana):
            for j in range(cantChoferes):
                kmCh += kilometros[j][i]
                sumaKM[iKM] = kmCh
        # print(sumaKM)

    #Sumo los kilometros totales y lo almaceno en "suma" para posteriormente hacer un promedio
    for i in range(cantChoferes):
        for j in range(diasSemana):
            suma += kilometros[i][j]
    promedioTotal=suma/cantChoferes
    # print(suma,promedioTotal)
    
    # input: nombre, kilometro
    # output: nombres, kilometros, totalRecorrido.
    # mejorCh, mayorKm.
    # promedioTotal
    
    print(f"""\n----------------------------------------------------------------------------------
          
Los choferes ingresados son {nombres} y recorrieron {suma} km entre los {cantChoferes}.
haciendo entre los {cantChoferes}, {promedioTotal}km en promedio.
el mejor chofer fue {mejorCh} habiendo hecho {mayorKM} el dia {jDia}.

----------------------------------------------------------------------------------\n""")
        
choferes()
    