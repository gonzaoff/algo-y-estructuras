def promAlt():
    cantEst=int(input("Cuantos estudiantes son: "))
    estudiantes = [float() for i in range(cantEst)]

    for altura in range(cantEst):
        datos=float(input("Ingrese la altura de los estudiantes: "))
        estudiantes[altura]=datos

    for altura in range(cantEst):
        sumaAltura=float()
        sumaAltura += estudiantes[altura]
        promedioAltura = sumaAltura / cantEst
    print(f"El promedio de altura es: {promedioAltura}")
    
    
    
    
    
    
    
    
def promAlt2():
    cant_est = int(input("Cuántos estudiantes son: "))

    alturas = [float() for i in range(cant_est)]
    for i in range(cant_est):
        altura = float(input(f"Ingrese la altura del estudiante {i+1}: "))
        alturas[i] = altura

    suma_alturas = 0.0 
    for i in range(cant_est):
        suma_alturas += alturas[i]

    promedio_altura = suma_alturas / cant_est

    print(f"El promedio de altura es: {promedio_altura}")

promAlt2()
    
#Escobar Gonzalo