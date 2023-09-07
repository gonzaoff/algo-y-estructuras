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

controlCalidad()

        