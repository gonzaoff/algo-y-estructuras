def regMultas():
    #input: cantMultas, dentro, DNI, tipoMulta(alta velocidad, mal estacionado, alcolemia positiva o semaforo en rojo)
    # si el infractor firmo o no la multa, el monto de la multa

    #output: mostrar en pantalla: cantidad total de multas por tipo, monto total y promedio por tipo, cantidad de infractores que firmaron
    # monto total de las multas
    tipoMul=0

    firma=""
    multa=""
    
    totalPMulta=0
    cantMultas=0

    valorAV=0
    cantAV=0
    totalAV=0

    valorSR=0
    cantSR=0
    totalSR=0

    valorME=0
    cantME=0
    totalME=0

    valorAP=0
    cantAP=0
    totalAP=0

    DNI=0

    cantMultas=input("Digite la cantidad de multas a registrar: ")
    if cantMultas != 0:
        for i in range(cantMultas):

            tipoMul=int(input("""Seleccione el tipo de multa:
1) Alta Velocidad.
2) Mal Estacionado.
3) Alcolemia Positiva.
4) Semaforo en Rojo. """))

            if tipoMul==1:
                cantAV=cantAV+1
                multa="Alta Velocidad"
                valorAV=int(input(f"Ingrese el valor de {multa}: "))

                firma=input("¿El infractor firmo la multa?")
                if firma =="si":
                    print("Multa agregada con exito.")
