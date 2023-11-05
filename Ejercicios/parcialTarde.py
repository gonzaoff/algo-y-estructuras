from os import system
system("cls")

def temper():
    
    temp=0
    suma=0
    bajoProm=0
    mayorTemp=0
    promedioTemp=0
    
    #determino la cantidad de dias en la que voy a trabajar 
    cantDias=int(input("ingrese los dias: "))
    temperaturas = [str() for i in range(cantDias)]
    
    #Ingreso los valores de temperatura en la array.
    for i in range(cantDias):
        temperatura = int(input(f"\nIngrese las temperaturas del dia {[i+1]} en grados centigrados: "))
        temperaturas[i] = temperatura
        temp += 1
    
    #Determino el dia de la mayor temperatura

        if temperatura > mayorTemp:
            mayorTemp = temperatura
            iDia = i
        #determino cuantos dias la temperatura estuvo debajo del promedio   
    #Sumo las temperaturas y promedio.
        suma += float(temperaturas[iDia]) 
        promedioTemp = suma / cantDias
    
        #si la temperatura encontrada en la array es menor que la temperatura promedio, se suma uno a cantidad dias bajo prom
        if temperaturas[iDia] < promedioTemp:
            bajoProm += 1
                
    print(f"la suma de las temperaturas es:{suma}, el promedi es: {promedioTemp}")
    print(f"la mayor temperatura fue {mayorTemp} el dia {iDia+1}")
    print(f"\nHubieron {bajoProm} dias bajo el promeedio") 
    
##Agregar modelo final
        
temper()