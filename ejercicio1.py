import os
os.system("cls")

def ventasDiarias():
    dia=0
    promedioTotal=0
    
    ventaDiaJU=0
    mayorVentaJU=0
    diaMayorJU=0
    totalVentaJU=0
    cantVentaJU=0
    promedioVentasJU=0
    
    ventaDiaAG=0
    mayorVentaAG=0
    diaMayorAG=0
    totalVentaAG=0
    cantVentaAG=0
    promedioVentasAG=0
    
    ventaDiaSE=0
    mayorVentaSE=0
    diaMayorSE=0
    totalVentaSE=0
    cantVentaSE=0
    promedioVentasSE=0
    
    mes=input("Ingrese el mes de ventas: ")
    
    while mes=="julio":
        
        dia=int(input("Ingrese el dia: "))
        
        while dia in range(1,32):
            
            print(f"{dia} de julio.")
            ventaDiaJU=int(input("Ingrese la venta del dia: \n"))
            
            cantVentaJU=cantVentaJU+1
            totalVentaJU=totalVentaJU+ventaDiaJU
            promedioVentasJU=totalVentaJU/cantVentaJU
            
            if mayorVentaJU<ventaDiaJU:
                mayorVentaJU=ventaDiaJU
                diaMayorJU=dia
                
            dia=int(input("Ingrese el dia(para continuar presione 0): \n"))
            
        if dia == 0:   
            
            print(f"El total vendido es {totalVentaJU}\n")
            print(f"La mayor venta de agosto fue: {mayorVentaJU} el dia {diaMayorJU}\n")
            print(f"el promedio de ventas de agosto es {promedioVentasJU}\n")
            
        mes=input("Ingrese el mes de ventas: \n")
        
    while mes=="agosto":
        
        dia=int(input("Ingrese el dia(para continuar presione 0): \n"))
        
        while dia in range(1,32):
            
            print(f"{dia} de agosto.\n")
            ventaDiaAG=int(input("Ingrese la venta del dia: \n"))
            
            cantVentaAG=cantVentaAG+1
            totalVentaAG=totalVentaAG+ventaDiaAG
            promedioVentasAG=totalVentaAG/cantVentaAG
            
            if mayorVentaAG<ventaDiaAG:
                mayorVentaAG=ventaDiaAG
                diaMayorAG=dia
                
            dia=int(input("Ingrese el dia(para continuar presione 0): \n"))
            
        if dia == 0:     
            
            print(f"El total vendido es {totalVentaAG}\n")
            print(f"La mayor venta de agosto fue: {mayorVentaAG} el dia {diaMayorAG}\n")
            print(f"el promedio de ventas de agosto es {promedioVentasAG}\n")
            
        mes=input("Ingrese el mes de ventas: ")
        
    while mes=="septiembre":
        
        dia=int(input("Ingrese el dia(para continuar presione 0): \n"))
        
        while dia in range(1,32):
            
            print(f"{dia} de septiembre.")
            ventaDiaSE=int(input("Ingrese la venta del dia: \n"))
            
            cantVentaSE=cantVentaSE+1
            totalVentaSE=totalVentaSE+ventaDiaSE
            promedioVentasSE=totalVentaSE/cantVentaSE
            
            if mayorVentaSE<ventaDiaSE:
                mayorVentaSE=ventaDiaSE
                diaMayorSE=dia
                
            dia=int(input("Ingrese el dia(para continuar presione 0): \n"))     
            
        if dia == 0:        
            
            print(f"El monto total es {totalVentaSE}\n")
            print(f"La mayor venta de agosto fue: {mayorVentaSE} el dia {diaMayorSE}\n")
            print(f"el promedio de ventas de agosto es {promedioVentasSE}\n")
        mes=input("""Ingrese el mes de ventas (para ver los promedios escriba "promedio"): \n""")
        
    while mes == "promedio":
        
        print(f"el promedio del trimestre fue {promedioTotal}\n")
        if mayorVentaSE<mayorVentaAG:
            mes="septiembre"
            mayorVentaTotal=totalVentaSE
            mayorDia=diaMayorSE
        
        elif mayorVentaJU<mayorVentaSE:
            mes="julio"
            mayorVentaTotal=ventaDiaJU
            mayorDia=diaMayorJU
        
        else:
            mes="agosto"
            mayorVentaTotal=ventaDiaAG
            mayorDia=diaMayorAG
        
        print(f"el dia {mayorDia}, del mes {mes}, se vendio {mayorVentaTotal}\n")
        print(f"el promedio del trimestre fue {promedioTotal}\n")
        print(f"el dia {mayorDia}, del mes{mes}, se vendio {mayorVentaTotal}\n")


