def controlCalidad():
    # Tengo que pedir la cantidad de piezas
    # para cada pieza tengo que pedir 
    # "Largo" y "Ancho"
    totalLargo=0
    totalAncho=0
    piezaDescartada=0
    cantPiezas=1
    while cantPiezas != 0:
        ancho=float(input(f"Ingrese el ancho de la pieza: "))
        largo=float(input(f"Ingrese el largo de la pieza: "))
        if ancho >= 4 and ancho <= 4.6 and largo >=15 and largo <= 15.6:
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

controlCalidad()

def controlCalidad2():

    totalLargo=0
    totalAncho=0
    piezaDescartada=0
    totalLarPromedio=0
    totalAnPromedio=0

    ancho=float(input("Ingrese el ancho de la pieza : "))
    largo=float(input("Ingrese el largo de la pieza : "))
    condicionAncho=ancho >= 4 and ancho <= 4.6 and ancho != 0
    condicionLargo=largo >=15 and largo <= 15.6 and largo != 0

    while condicionLargo and condicionAncho:

        ancho=float(input("Ingrese el ancho de la pieza : "))
        largo=float(input("Ingrese el largo de la pieza : "))

        cantPiezas=+1
        totalLargo=totalLargo+largo
        totalAncho=totalAncho+ancho
        totalLarPromedio=totalLargo/cantPiezas
        totalAnPromedio=totalAncho/cantPiezas
        
        while ancho != condicionAncho or largo != condicionLargo:
            piezaDescartada=+1
            print(f"{piezaDescartada} Piezas descartadas")



# controlCalidad2()
        