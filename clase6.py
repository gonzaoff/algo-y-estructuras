from os import system
system("cls")

def HorasTrabajo():
    pagoPorHora=int(input("Ingrese el pago por hora: "))
    
    if pagoPorHora!=0:
        horasTrabajadas=0
        dias=0
        
        for dias in range(6):
            horasTrabajadas=int(input(f"ingrese las horas trabajadas del dia {dias+1}: "))
            dias += 1

        sueldo = horasTrabajadas*pagoPorHora*dias
        print(sueldo)
        
    else:
        print("Ingrese un valor valido.")

# HorasTrabajo()

#debo saber: cuantas ventas son mayores a $1000
#cuantas mayores a 500 pero igual o menores a $1000
#cuantas menores o iguales a 500.
#determinar el total de cada una

def VentasTienda():
    
    ventas=0
    cantidadDeMil=0
    cantidadDeQuinientos=0
    menorQueQuinientos=0
    total=0

    for ventas in range(3):
        
        ventas = int(input("ingrese la venta: del dia: "))

        if ventas > 1000:
            cantidadDeMil+=1

        if ventas > 500 and ventas <= 1000:
            cantidadDeQuinientos+=1

        if ventas <= 500:
            menorQueQuinientos+=1

        total=total + ventas

    print(f"""----------------------
la cantidad de ventas mayores a $1000 son: {cantidadDeMil}
la cantidad de ventas mayores a $500 pero igual o menores a $1000 son: {cantidadDeQuinientos} 
la cantidad de ventas menores o iguales a $500: {menorQueQuinientos}
la cantidad total vendida es de: ${total}""")

# VentasTienda()

#tengo que contar un lote de 12 focos y el numero de focos
#que hay en cada existencia
def contar_focos():
    total=0
    focoVerde=0
    focoBlanco=0
    focoRojo=0
    totalrojo=0
    totalblanco=0
    totalverde=0
    for _ in range(12):
        colorFocos = int(
            input(
                """----------------
1) Verde.
2) Rojo
3) Blanco
Ingrese el valor del color elegido: """
            )
        )
        focoVerde=0
        focoBlanco=0
        focoRojo=0
        if colorFocos == 1:
            focoVerde =+1
        elif colorFocos == 2:
            focoRojo=+1
        elif colorFocos == 3:
            focoBlanco =+1
        totalverde = totalverde + focoVerde
        totalrojo = totalrojo + focoRojo
        totalblanco = totalblanco + focoBlanco
    print(f"""-----------------
La cantidad de focos blancos es: {totalblanco}
la cantidad de focos verdes es: {totalverde}
la cantidad de focos rojos es: {totalrojo}""")
contar_focos()