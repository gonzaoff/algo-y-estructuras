from os import system
system("cls")

def ventasAH():

    selector=0
    selector2=0
    regLit=0
    regCen=0
    regBS=0
    regCABA=0
    regNorOes = 0
    regNoreste = 0 
    regNor=0
    regCentro=0
    regSur=0

    totalVentLit=0
    totalVentCen=0
    totalVentBS=0
    totalVentCABA=0
    totalVentNorOes=0
    totalVentNoreste=0
    totalVentCentro = 0
    totalVentNor = 0
    totalVentSur = 0
    
    cantVenLit=0
    cantVenCen=0
    cantVenBS=0
    cantVenCABA=0
    cantVenNorOes=0
    cantVenNoreste=0
    cantVentCentro = 0
    cantVentNor = 0
    cantVentSur = 0

    promNor=0
    promCen=0
    promSur=0
    promLit=0
    promCentro=0
    promBS=0
    promCABA=0
    promNorOes = 0
    promNoreste = 0 

    CanTotalVenLit=0
    CanTotalVenCen=0
    CanTotalVenCentro=0
    CanTotalVenBS=0
    CanTotalVenCABA=0
    CanTotalVenNorOes = 0
    CanTotalVenNoreste = 0 

    
    #1) input: ventas por sucursal.
    #2) output: registrso de venta mensuales de cada region (8 regiones).

    
    mes=input("Ingrese el mes: ")
    if mes == "enero" or mes == "salir":

        selector=int(input("""Ingrese la opcion adecuada:
                        1) Ventas por sucursal
                        2) Reg de ventas mensuales.
                        3) Promedio de ventas""")) 
        
        while selector == 1:

            region = str(input("Ingrese la región"))

            while region == 'Región litoral' or region != "salir":
                    
                    CanTotalVenLit = cantVenLit + 1 
                    regLit = float(input("Ingrese el monto de venta: ")) 
                    while regLit != 0:
                          
                        totalVentLit=totalVentLit+regLit
                        regLit = float(input("Ingrese el monto de venta (precione 0 para ver los promedios): "))

                    promLit=totalVentLit/CanTotalVenLit
                    print(promLit)

            while region == 'Región centro' or region != "salir":

                    CanTotalVenCen = cantVenCen + 1 
                    regCen = float(input("Ingrese el monto de venta: ")) 
                    while regCen != 0:
                          
                        totalVentCen=totalVentCen+regCen
                        regCen = float(input("Ingrese el monto de venta (precione 0 para ver los promedios): "))

                    promCen=totalVentCen/CanTotalVenCen
                    print(promNorOes)

            while region == 'región de provincia de buenos aires' or region != "salir":

                    CanTotalVenBS = cantVenBS + 1 
                    regBS = float(input("Ingrese el monto de venta: ")) 
                    while regBS != 0:
                          
                        totalVentBS=totalVentBS+regBS
                        regBS = float(input("Ingrese el monto de venta (precione 0 para ver los promedios): "))

                    promBS=totalVentBS/CanTotalVenBS
                    print(promBS)
                    
            while region == 'región de ciudad de buenos aires' or region != "salir":

                    CanTotalVenCABA = cantVenCABA + 1 
                    regCABA = float(input("Ingrese el monto de venta: ")) 
                    while regCABA != 0:
                          
                        totalVentCABA=totalVentCABA+regCABA
                        regCABA = float(input("Ingrese el monto de venta (precione 0 para ver los promedios): "))

                    promCABA=totalVentCABA/CanTotalVenCABA
                    print(promCABA)
                    
            while region == 'región nordeste' or region != "salir":

                    CanTotalVenNoreste = cantVenNoreste + 1 
                    regNoreste = float(input("Ingrese el monto de venta: ")) 
                    while regNoreste != 0:
                          
                        totalVentNoreste=totalVentNoreste+regNoreste
                        regNoreste = float(input("Ingrese el monto de venta (precione 0 para ver los promedios): "))

                    promNoreste=totalVentNoreste/CanTotalVenNoreste
                    print(promNoreste)

            while region == 'región noroeste' or region != "salir":
                    
                    CanTotalVenNorOes = cantVenNorOes + 1 
                    regNorOes = float(input("Ingrese el monto de venta: ")) 
                    while regNorOes != 0:
                          
                        totalVentNorOes=totalVentNorOes+regNorOes
                        regNorOes = float(input("Ingrese el monto de venta (precione 0 para ver los promedios): "))

                    promNorOes=totalVentNorOes/CanTotalVenNorOes
                    print(promNorOes)
                    


            selector=int(input("""Ingrese la opcion adecuada:
1) Ventas por sucursal
2) Reg de ventas mensuales.
2) Promedio de ventas""")) 

        #3) output: promedio de ventas de cada region (3) y promedio total.        
        if selector == 2 :

            promNor=totalVentNor/cantVentNor
            promCentro=totalVentCentro/cantVentCentro
            promNor=totalVentSur/cantVentSur

            promE=promSur+promNor+promCentro

            #promE va a agregar sus valores a una lista

            print(f"***************")
            print(f"PROMEDIOS por Región")
            print(f"***************")
            print(f"NORTE: $ {promNor}")
            print(f"CENTRO: $ {promCentro}")
            print(f"SUR: $ {promSur}")
            print(f"***************")
            print(f"PROMEDIOS Mensuales (Todo el país)")
            print(f"***************")
            print(f"1: $ {promE}")
            print(f"2: $ {promE}.")

            selector=int(input("""Ingrese la opcion adecuada:
        1) Ventas por sucursal
        2) Reg de ventas mensuales.
        2) Promedio de ventas"""))

        if selector == 3:
              



        #4) output: maximo y minimo de cada region en que mes.


ventasAH()



