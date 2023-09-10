from os import system
system("cls")

def controlCalidad():
    totalLargo=0
    totalAncho=0
    piezaDescartada=0
    cantPiezas=1
    while cantPiezas != 0:
        ancho=float(input(f"Ingrese el ancho de la pieza: "))
        largo=float(input(f"Ingrese el largo de la pieza: "))
        condAncho=ancho >= 4 and ancho <= 4.6
        condLargo=largo >=15 and largo <= 15.6
        if condAncho and condLargo:
            totalLargo=totalLargo+largo
            totalAncho=totalAncho+ancho
            cantPiezas=cantPiezas+1
            print("Pieza añadida correctamente")
        else:
            piezaDescartada=piezaDescartada+1
            print(f"Piezas descartadas: {piezaDescartada}")
        
        if ancho == 0 and largo == 0:
            totalLarPromedio=totalLargo/cantPiezas
            totalAnPromedio=totalAncho/cantPiezas
            print(f"""--------------------------------------
        la cantidad de piezas ingresadas: {cantPiezas}
        la cantidad de piezas descartadas: {piezaDescartada}
        en promedio el largo es: {totalLarPromedio}
        en promedio el ancho es: {totalAnPromedio}""")

# controlCalidad()

def datosSalud():
    #Input=DNI,Nombre,Edad,Peso,Altura,Sexo
    
    cantEmpleados=0
    cantEdad=0
    cantM=0
    cantH=0
    promEdad=0
    promPesoH=0
    promPesoM=0
    pesoTotalH=0
    pesoTotalM=0

    dni=float(input("Ingrese su DNI (para finalizar precione 0): "))

    while dni != 0:

        cantEmpleados=cantEmpleados+1
        
        nombre=input("Ingrese su nombre:")

        edad=int(input("Ingrese su edad:"))

        if edad != 0:
            cantEdad=cantEdad+1
            promEdad=promEdad+edad

        sexo=input("Ingrese su sexo(en minusculas): ")

        if sexo == "masculino"or"hombre":
            peso=float(input("Ingrese su peso en Kg (con punto, no coma): "))
            pesoTotalH=pesoTotalH+peso
            cantH=cantH+1
            promPesoH=pesoTotalH/cantH
        elif sexo =="femenino"or"mujer":
            peso=float(input("Ingrese su peso en Kg (con punto, no coma): "))
            pesoTotalM=pesoTotalM+peso
            cantM=cantM+1
            promPesoM=pesoTotalM/cantM
            

        altura=float(input("Ingrese su altura (con punto, no coma): "))

        dni=float(input("Ingrese su DNI (para finalizar precione 0): "))
        #Output=cantidad de empleados, promedio edad, promedio peso discriminando sexo.
    print(f"""---------------------------------
La cantidad de empleados: {cantEmpleados}
El promedio de edad es: {promEdad}
El promedio de peso en hombre: {promPesoH}
El promedio de peso en mujeres es: {promPesoM}
---------------------------------""")
    
# datosSalud()

def ventasTele():
    #Input: ventas 
    #output: Monto total de ventas, "si" el monto es mayor a 500, es "optimo"
    totalVentas=0
    ventas=int(input("Ingrese la venta(ingrese 0 para continuar):"))
    
    while ventas!=0:
        totalVentas=totalVentas+ventas
        ventas=int(input("Ingrese la venta(ingrese 0 para continuar):"))

        if ventas > 500000:
            print("El valor es optimo")
            ventas=int(input("Ingrese el valor de la venta(ingrese 0 para continuar)"))
        if ventas == 0:
            print(f"La venta total es de:{totalVentas}")
    

# ventasTele()

def numerosPares():
    numero=int(input("Ingrese el numero: "))
    if numero %2>0:
        print(f"el numero {numero} es impar.")
    else:
        print(f"el numero {numero} es par")

# numerosPares()

# def numeroPares2():
#     for i in range(2,20,2):

def comparacion():
    n= int(input("cuantos numeros se compararan: "))
    mayor=int(input("ingrese el numero: "))
    for i in range(n-1):
        numero = int(input("ingrese el numero: "))
        if numero > mayor:
            mayor = numero
    print(f"el numero mayor es : {mayor}")
            
# comparacion()

def MayorYMenor():
    n=int(input("cuantos numeros se compararan: "))
    mayor=int(input("ingrese el numero: "))
    menor = mayor

    for i in range(n-1):
        numero = int(input("ingrese el numero: "))

##si el numero sea mayor que "Mayor", "Mayor" igual a "numero"
##si el numero sea menor que "Menor", "Menor" igual a numero
        if numero < menor:
            menor = numero
        if numero > mayor:
            mayor = numero

    print(f"""el numero mayor es: {mayor}
el numero menor es: {menor}""")

MayorYMenor()

def longItud():
    #input: cantidad de piezas a procesar, la logitud de cada perfil,
    #solo "si" se encuentra entre 1,20 y 1,30

    #output: la cantidad de piezas aptas
    totalPiezas=0
    cantPiezas=int(input("Ingrese la cantidad de piezas:"))

    for i in range(cantPiezas-1)
    
        tamaño=int(input("Ingrese la longitud en mts: "))

        if tamaño <= 1.20 and tamaño>=1.30:
            totalPiezas=totalPiezas+1
            tamaño
    print

        