def regMultas():
    #input: cantMultas, dentro, DNI, tipoMulta(alta velocidad, mal estacionado, alcolemia positiva o semaforo en rojo)
    # si el infractor firmo o no la multa, el monto de la multa

    #output: mostrar en pantalla: cantidad total de multas por tipo, monto total y promedio por tipo, cantidad de infractores que firmaron
    # monto total de las multas
    tipoMul=0

    firma=""
    totalFirmas=0
    multa=""

    promedioMultas=0
    totalPMulta=0
    cantMultas=0

    valorAV=0
    cantAV=0
    totalAV=0
    sumaTotalAV=0
    promedioAV=0

    valorSR=0
    cantSR=0
    totalSR=0
    promedioSR=0

    valorME=0
    cantME=0
    totalME=0
    promedioME=0

    valorAP=0
    cantAP=0
    totalAP=0
    promedioAP=0

    DNI=0

    cantMultas=input("Digite la cantidad de multas a registrar: ")
    if cantMultas != 0:

        DNI=int(input("Ingrese el DNI del infractor: "))

        for _ in range(cantMultas):
            tipoMul=int(input("""Seleccione el tipo de multa:
1) Alta Velocidad.
2) Mal Estacionado.
3) Alcolemia Positiva.
4) Semaforo en Rojo. """))


            if tipoMul==1:

                cantAV=cantAV+1
                multa="Alta Velocidad"
                valorAV=int(input(f"Ingrese el valor de {multa}: "))

                sumaTotalAV=valorAV*cantAV
                promedioAV=sumaTotalAV/cantAV

                print("La multa fue agregada con exito.")

            elif tipoMul == 2:

                cantME=cantME+1
                multa="Alta Velocidad"
                valorME=int(input(f"Ingrese el valor de {multa}: "))

                sumaTotalME=valorME*cantME
                promedioME=sumatotalME/cantME

                print("La multa fue agregada con exito.")

            elif tipoMul == 3:

                cantSE=cantSE+1
                multa="Alta Velocidad"
                valorSE=int(input(f"Ingrese el valor de {multa}: "))

                sumaTotalSE=valorSE*cantSE
                promedioSE=sumaTotalSE/cantSE

                print("La multa fue agregada con exito.")

            elif tipoMul == 4:

                cantAP=cantAP+1
                multa="Alta Velocidad"
                valorAV=int(input(f"Ingrese el valor de {multa}: "))

                sumaTotalAP=valorAP*cantAP
                promedioAP=sumaTotalAP/cantAP

                print("La multa fue agregada con exito.")

        firma=input("¿El infractor firmo las multas?")
        if firma == "si":
            totalFirmas += 1

        promedioMultas=(sumaTotalAP+sumaTotalAV+sumaTotalME+sumaTotalSE)/cantMultas
        
            
            
