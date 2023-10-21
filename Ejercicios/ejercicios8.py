
from os import system
system("cls")

def choferes():  # sourcery skip: convert-to-enumerate, move-assign-in-block, use-itertools-product

    #indices:
    iKM=0
    iCam=0
    jDia=0
    
    #variables preinicializadas
    suma=0
    diasSemana=6
    mayorHR=0
    kmCh=0
    
    #ingreso la cantidad de choferes
    cantChoferes=3 #int(input("Ingrese la cantidad de choferes: "))
    
    sueldo=300 #int(input("ingrese el sueldo por hora"))
    
    #inicializo las arrays/matrices
    nombres=[str() for i in range(cantChoferes)]
    dias = [[0.0] * diasSemana for i in range(cantChoferes)]
    sumaKM=[float() for i in range(cantChoferes)]

    #solicito el nombre del chofer con la variable "nombre" y lo almaceno en la array "nombres" con el indice "iN"
    for i in range(cantChoferes):
        nombre=str(input("\nIngrese el nombre del chofer: "))
        nombres[i]=nombre
        
        # print(nombres)
        
        #solicito el kilometraje del chofer con la variable "kilometro" y lo almaceno en la array "kilometros" con los indices "[i][j]"
        for j in range(diasSemana):
            dia=float(input(f"\ningrese las horas trabajadas el dia el dia {j+1}: "))
            dias[i][j] = dia 
            
            # si la variable "kilometro" es mayor a "mayorKM" entonces almaceno el valor de "kilometro" en "mayorKM",  
            # el indice del nombre del chofer "i" en "iCam", guardo su valor en "mejorCh", y el dia "j+1" en "jDia"
            if dia > mayorHR:
                mayorHR = dia
                iCam = i
                jDia = j+1
                mejorCh = nombres[iCam]
        # print(kilometros)
        

    #Sumo los kilometros totales y lo almaceno en "suma" para posteriormente hacer un promedio

    for i in range(cantChoferes):
        for j in range(diasSemana):
            suma += dia[i][j] * sueldo
            suma
    promedioTotal=suma/cantChoferes
    # print(suma,promedioTotal)
    

    print(f"""\n----------------------------------------------------------------------------------
          
Los choferes ingresados son {nombres} y recorrieron {suma} km entre los {cantChoferes}.
haciendo entre los {cantChoferes}, {promedioTotal}km en promedio.
el mejor chofer fue {mejorCh} habiendo hecho {mayorHR} el dia {jDia}.

----------------------------------------------------------------------------------\n""")
        
# choferes()
    




miLista = [1,3,5,2,7,8,9]

def listaNumerosASumar(listas,objetivo):
    #input: listaNumerosASumar, objetivoNumerico
    
    tamañoLista = len(listas)
    valoresSumablesA = []
    valoresSumablesB = []
    cantidadDeNumerosMenorAlObjetivo=0
    resultado=[[0] for i in range(tamañoLista)]
                
    for i in range(tamañoLista):
        if listas[i] < objetivo:
            resultado.append(listas[i])


                

            

        
    print(resultado)

listaNumerosASumar(miLista,6)
    