from os import system
system("cls")

def invertido():
    
    #dado un vectorA de 10 posiciones
    vectorA = [1,2,3,4,5,6,7,8,9,10]

    #agregar esos valores a un vectorB
    vectorB = [int() for i in range(10)]

    j=9 #indice del array donde queremos mandar los valores, debe estar uno por debajo del rango

    #mientras el indice donde estan los valores sea menor al rango
    for i in range(10):
        #la variable auxiliar almacena el primer valor del vector donde estan los valores
        traspaso = vectorA[i]
        # print(traspaso)

        # Quita los valores del primer vector hacia el ex vector vacio
        # vectorA[i] = vectorB[j]
        # print(vectorA,vectorB)

        # el vector vacio, almacena los valores
        vectorB[j] = traspaso
        #el indice donde se almacenan los valores decrementa (j Z- 1)
        j = j - 1

    print(vectorA,vectorB)    
# invertido()


def vivienda():  # sourcery skip: collection-into-set, merge-comparisons

    #Condicionales:
    menorU=0
    hastaTres=0
    hastaSeis=0
    masDeSeis=0
    
    #Constantes:
    smvm=84.512
    recordatorio="Recuerde responder en mayusculas"
    
    #Variables Mayores:
    mayorEdad = 0
    mayorBarrio = str()
    mayorIngreso = 0
    mayorNivelEd = str()
    mayorOrgViv = str()

#   Inicializo y determino el tamaño de las arrays
    cantPersonas=int(input("Ingrese cuantas personas fueron censadas: "))

#   Inicializo las arrays en funcion de la determinacion anterior
    edades=[int() for i in range(cantPersonas)]
    barrios=[str() for i in range(cantPersonas)]
    ingresos=[float() for i in range(cantPersonas)]
    nivelesEd=[str() for i in range(cantPersonas)]
    orgVivs=[str() for i in range(cantPersonas)]
    
#   comienzo a solicitar los datos en el rango determinado como "cantPersonas"
    for i in range(cantPersonas):
        edad=int(input(f"\nIngrese la edad del sujeto {i+1}: "))
        barrio=str(input(f"\nIngrese el nombre del barrio del sujeto {i+1}: "))
        ingreso=float(input(f"\nDetermine los ingresos familiares del sujeto {i+1} $: "))
        nivelEd=str(input(f"""\n{recordatorio}\nIngrese el nivel educativo del sujeto {i+1}\n(Primario(P) | Secundario(S) | Terciario(T) | Universitario(U)): """))
        orgViv=str(input(f"\n{recordatorio}\nDetermine el origen de la vivienda del sujeto {i+1}\n(Propia(P) | Alquilada(A) | Prestada(Pr)): "))

#       determino la cantidad de SMVI
        cantSMVM= ingreso/smvm

#       si es menor que 1 SMVM
        if cantSMVM < 1:
            menorU += 1
            # print("\nSe añadio a 'menos de 1 SMVM'")
            
#       si es igual o menor a 3 SMVM
        elif cantSMVM <= 3:
            hastaTres += 1
            # print("\nSe añadio a 'entre 1 a 3 SMVM'")
            
#       si es menor o igual a 6 SMVM
        elif cantSMVM <= 6:
            hastaSeis += 1
            # print("\nSe añadio a 'entre 3 a 6 SMVM'")

#       si es mayor a 6 SMVM
        else:
            masDeSeis += 1
            # print("\nSe añadio a 'mas de 6 SMVM'")

#       Identificadores para guardado en Array
        if nivelEd == "P":
            nivelEd = "Primaria"
        elif nivelEd == "S":
            nivelEd = "Secundaria"
        elif nivelEd == "T":
            nivelEd = "Terciaria"
        elif nivelEd == "U":
            nivelEd = "Universitaria"

        # Identificadores para guardado en Array
        if orgViv == "P":
            orgViv = "Propia"
        elif orgViv == "A":
            orgViv = "Alquilada"
        elif orgViv == "Pr" or orgViv == "PR":
            orgViv = "Prestada"

        # Determino el ingreso mayor y guardo las variables que necesito mostrar.
        # (edad, barrio, ingreso, nivel educativo y origen de vivienda)
        if ingreso > mayorIngreso:
           mayorEdad = edad
           mayorBarrio = barrio
           mayorIngreso = ingreso
           mayorNivelEd = nivelEd
           mayorOrgViv = orgViv

        edades[i] = edad
        barrios[i] = barrio
        ingresos[i] = ingreso
        nivelesEd[i] = nivelEd
        orgVivs[i] = orgViv

        i += 1
    
    print(f"""------------------------------------------
\nPersonas Censadas : {cantPersonas}\n
Personas con Menos de 1 SMVM: {menorU}\n
Personas entre 1 y 3 SMVM: {hastaTres}\n
Personas entre 3 y 6 SMVM: {hastaSeis}\n
Personas con mas de 6 SMVM: {masDeSeis}\n
La persona con el mayor ingreso tiene: {mayorEdad} años.\nVive en el barrio: "{mayorBarrio}".\nPosee educacion: {mayorNivelEd}\nEl origen de su vivienda es: {mayorOrgViv}\n
>------------------------------------------""")

# vivienda()

def notas2():  # sourcery skip: use-itertools-product
    
    #Variables de mejores.
    mejorNota=0
    mejorProm=0
    mejorMat=str()
    mejorAlu=str()
    
    #Variables de menores.
    menorNota=10
    menorProm=10
    menorMat=str()
    menorAlu=str()
    
    #Promedios y sumadores.
    promedioAlu=0
    sumaAlu=0
    sumaMat=0
    promedioMat=0
    
    #Solicito la cantidad de alumnos para establecer el tamaño de mi array "cantAlumnos"
    cantAlumnos=int(input("Ingrese la cantidad de alumnos: "))

    #Inicializo mi array
    alumnos=[str() for i in range(cantAlumnos)]

    # Solicito el nombre de los alumnos y las guardo en la array "alumnos"
    for i in range(cantAlumnos):
        alumno=str(input(f"\nIngrese el nombre del alumno {i+1}: "))
        alumnos[i]=alumno
    print(alumnos)
    
    #Solicito la cantidad de materias para establecer el tamaño de mi array "materias"
    cantMaterias=int(input("Ingrese la cantidad de materias: "))
    materias=[str() for i in range(cantMaterias)]  

    # Solicito el nombre de las materias y las almaceno en la array "materias"
    for j in range(cantMaterias):
        materia=str(input(f"\nIngrese el nombre de la materia {j+1}: "))
        materias[j]=materia
    print(materias)
    
    #Inicializo la matriz "notas"
    notas=[[0.0] * cantMaterias for i in range(cantAlumnos)]
    
    #Solicito las notas y las guardo en la matriz "notas"
    for i in range(cantAlumnos):
        for j in range(cantMaterias):
            
            nota=float(input(f"\nIngrese las notas de {alumnos[i]} para {materias[j]} "))

            #almaceno las notas en la matriz
            notas[i][j]=nota
            
        #Si la variable notas en mayor a la nota mayor, almacena los datos de "nota, alumnos[i] y materias[j]"
            if nota > mejorNota:
                mejorNota = nota
                mejorAlu = alumnos[i]
                mejorMat = materias[j]
            
            #Si la variable menorNotas en mayor a la nota, almacena los datos de "nota, alumnos[i] y materias[j]"
            if nota < menorNota:
                menorNota = nota
                menorAlu = alumnos[i]
                menorMat = materias[j]

    print("------------------------------------------------------------------------------------------")
    #Sumo y promedio las notas de los alumnos.
    for i in range(cantAlumnos):
        for j in range(cantMaterias):
            sumaAlu+=notas[i][j]
        promedioAlu=sumaAlu/cantMaterias
        
        #si menorPromedio es mayor a promedioAlu, menor promedio es igual a promedioAlu  
        if promedioAlu < menorProm:
            menorProm = promedioAlu
        
        #si promedioAlu es mayor a mejorProm, mejorProm es igual a promedioAlu
        if promedioAlu > mejorProm:
            mejorProm = promedioAlu
            
        print(f"Promedio {alumnos[i]}: {promedioAlu}\n")
        #reinicio el sumador.
        sumaAlu=0
        
    #Sumo y promedio las notas por materia.
    for i in range(cantMaterias):
        for j in range(cantAlumnos):     
            sumaMat+=notas[j][i]
        promedioMat=sumaMat/cantAlumnos
        print(f"Promedio {materias[i]}: {promedioMat}\n")
        sumaMat=0

    #Muestro en pantalla los resultados
    print(f"Nota Sobresaliente: {mejorAlu} {mejorNota} {mejorMat} Promedio: {mejorProm}\n")
    if menorProm < 5:
        print(f"\nRefuerzo: {menorAlu} {menorNota} {menorMat} Promedio: {menorProm}\n")
notas2()