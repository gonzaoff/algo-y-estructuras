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
    
    mayorNota=0
    mejorAlu=str()
    
    
    cantAlumnos=int(input("Ingrese la cantidad de alumnos: "))

    
    alumnos=[str() for i in range(cantAlumnos)]



    
    for i in range(cantAlumnos):
        alumno=str(input(f"\nIngrese el nombre del alumno {i+1}: "))
        alumnos[i]=alumno
    print(alumnos)
    
    cantMaterias=int(input("""\nIngrese la "CANTIDAD" de materias: """))
    materias=[str() for i in range(cantMaterias+1)]
    materias[0]="Alumno/materia"
        
    for j in range(cantMaterias):
        materia=str(input(f"\nIngrese el nombre de la materia {j+1}: "))
        materias[j+1]=materia
    print(materias)
    
    notas=[[0.0] * cantMaterias for i in range(cantAlumnos)]
    
    for i in range(cantAlumnos):
        for j in range(cantMaterias):
            
            nota=float(input(f"Ingrese las notas de {alumnos[i]} para {materias[j+1]} "))

            if nota > mayorNota:
                mayorNota = nota
                mejorAlu = alumnos[i]

            notas[i][j]=nota
            
    print(mayorNota,mejorAlu)    
    print(notas)
            
# output:
# promedio por alumno -> promAlu
# promedio por materia -> promedioMat
# nombre y promedio mejor alumno -> mejorProm
    
notas2()