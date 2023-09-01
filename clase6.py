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

HorasTrabajo()