def regMultas():
    #input: cantMultas, dentro, DNI, tipoMulta(alta velocidad, mal estacionado, alcolemia positiva o semaforo en rojo)
    # si el infractor firmo o no la multa, el monto de la multa

    #output: mostrar en pantalla: cantidad total de multas por tipo, monto total y promedio por tipo, cantidad de infractores que firmaron
    # monto total de las multas
    tipoMul=0

    infractores=0
    firma=""
    totalFirmas=0
    multa=""

    totalMultas=0
    promedioMultas=0
    cantMultas=0

    valorAV=0
    cantAV=0
    sumaTotalAV=0
    promedioAV=0

    valorSE=0
    cantSE=0
    sumaTotalSE=0
    promedioSE=0

    valorME=0
    cantME=0
    sumaTotalME=0
    promedioME=0

    valorAP=0
    cantAP=0
    sumaTotalAP=0
    promedioAP=0

    DNI=0


    
    cantMultas=int(input("Digite la cantidad de multas a registrar: "))
    if cantMultas != 0:
        
        DNI=int(input("Ingrese el DNI del infractor(sin puntos): "))
        if DNI != 0 or DNI < 99999999:
            infractores=+1
            for _ in range(cantMultas):
                tipoMul=int(input("""Seleccione el tipo de multa:
    1) Alta Velocidad.
    2) Mal Estacionado.
    3) Semaforo en Rojo.
    4) Alcoholemia Positiva. 
    """))
            
                if tipoMul==1:
                    cantAV=cantAV+1
                    multa="Alta Velocidad"
                    valorAV=int(input(f"Ingrese el valor de {multa}: "))
                    sumaTotalAV=valorAV*cantAV
                    promedioAV=sumaTotalAV/cantAV
                    print("La multa fue agregada con exito.")
                    
                elif tipoMul == 2:
                    cantME=cantME+1
                    multa="Mal Estacionado"
                    valorME=int(input(f"Ingrese el valor de {multa}: "))
                    sumaTotalME=valorME*cantME
                    promedioME=sumaTotalME/cantME
                
                elif tipoMul == 2:
                    cantME=cantME+1
                    multa="Alta Velocidad"
                    valorME=int(input(f"Ingrese el valor de {multa}: "))
                    
                    sumaTotalME=valorME*cantME
                    promedioME=sumaTotalME/cantME
                    print("La multa fue agregada con exito.")
                    
                elif tipoMul == 3:
                    cantSE=cantSE+1
                    multa="Semaforo en Rojo"
                    valorSE=int(input(f"Ingrese el valor de {multa}: "))
                    sumaTotalSE=valorSE*cantSE
                    promedioSE=sumaTotalSE/cantSE
                    print("La multa fue agregada con exito.")
                    
                elif tipoMul == 4:
                    cantAP=cantAP+1
                    multa="Alcolemia Positiva"
                    valorAV=int(input(f"Ingrese el valor de {multa}: "))
                    sumaTotalAP=valorAP*cantAP
                    promedioAP=sumaTotalAP/cantAP
                    print("La multa fue agregada con exito.")
                    
                totalMultas=sumaTotalAP+sumaTotalAV+sumaTotalME+sumaTotalSE
                
            firma=input("¿El infractor firmo las multas?")
            if firma == "si":
                totalFirmas =+ 1
                
            promedioMultas=totalMultas/cantMultas
    #output: mostrar en pantalla: cantidad total de multas por tipo, monto total y promedio por tipo, cantidad de infractores que firmaron
            print(f"""------------------------------------------
    Multas por Alta Velocidad: {cantAV}
    Multas por Alcolemia Positiva: {cantAP}
    Multas por Mal Estacionado: {cantME}
    Multas por Semaforo en Rojo: {cantSE}
    Total por Alta velocidad: {sumaTotalAV}         
    Total por Alcolemia Positiva: {sumaTotalAP}         
    Total por Mal Estacionado: {sumaTotalME}         
    Total por Semaforo en Rojo: {sumaTotalSE}         
    Promedio por Alta Velocidad: {promedioAV}         
    Promedio por Alcolemia Positiva: {promedioAP}         
    Promedio por Mal Estacionado: {promedioME}         
    Promedio por Semaforo en  rojo: {promedioSE}
    Total de infracciones: {totalMultas}
    Precio promedio de infracciones: {promedioMultas}
    cantidad de infractores que firmaron: {totalFirmas}

    """)   

            DNI=float(input("Ingrese el DNI del infractor: "))
regMultas()
