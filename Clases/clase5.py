def Calificacion():
    nombre = input("Ingrese el nombre: ")
    nota = int(input("Ingrese la nota: "))
    if nota >= 6 :
        print(f"{nombre} esta aprobado, su nota es {nota}")
    else:
        print(f"{nombre} esta desaprobado, su nota es {nota}")


# Calificacion()

def ParOImpar():
    numero = int(input("Ingresa un numero: "))
    if numero % 2 == 0:
        print("el numero es par.")
    else:
        print("el numero es impar.")


# ParOImpar()


def ValorNumerico():
    numero = int(input())
    numero2 = int(input())
    numero3 = int(input())
    if numero > numero2:
        print(f"{numero} es el mayor")
    elif numero2 > numero3:
        print(f"{numero2} es mayor")
    elif numero3 > numero:
        print(f"{numero3} es mayor")
        
# ValorNumerico()


def ValorNumerico2():
    numero = int(input("ingresa un valor numerico: "))
    numero2 = int(input("ingresa un valor numerico: "))
    numero3 = int(input("ingresa un valor numerico: "))
    mayor=numero
    if mayor < numero2:
        mayor=numero2
        if mayor < numero3:
            mayor = numero3
            
    print(f"el numero mayor es: {mayor}")

# ValorNumerico2()


def precio():
    precio = int(input("Ingrese el precio del producto: "))
    if precio <= 200:
        porcentaje = 20
        nuevoprecio = precio - (precio * porcentaje) / 100
        print(nuevoprecio)
    else: 
        print(precio)

# precio()


def almacen():  # sourcery skip: extract-duplicate-method
    cantArticulos=int(input("Cuantos articulos tienes: "))
    precio = int(input("Cuanto es el importe total: "))
    if cantArticulos > 20:
        porcentaje = 20
        descuento = (precio * porcentaje) / 100
        nuevoprecio = precio - descuento
        print(nuevoprecio)
    elif cantArticulos <= 10:
        porcentaje = 5
        descuento = (precio * porcentaje) / 100
        nuevoprecio = precio - descuento
        print(nuevoprecio)


def precioBoleto():
    km=int(input("distancia a viajar en km: "))
    dias=int(input("Ingrese la cantidad dias: "))
    valxkm=2
    precio = km * valxkm
    porc = 30 if km>800 ^ dias > 7 else 0
    descuento = precio * 2 /100 * porc
    print(f"\n\nkm por vuelo: {km} \nPrecio unitario: {precio} \nDescuento: {descuento} \n\nPrecio final ida y vuelta: {precio*2-descuento}")

# precioBoleto()

def acumulador():
    # sourcery skip: aug-assign, for-index-underscore, while-to-for
    suma = 0
    acumulador = 0

    while acumulador < 10:
        num = int(input("ingrese un numero: "))
        suma = suma + num
        acumulador = acumulador + 1
    print(f"total: {suma}")

# acumulador()


ejercicio="""se ingresan montos de venta en el teclado. no se sabe la cantidad de ventas que se va a ingresar, cuando el operador hay ingresado todas las ventas
ingresa "0" como valor, determinar: 
a) cantidad de ventas ingresadas.
b) suma total de las ventas.
c) promedio de ventas."""

def montos():
    montos = float(input("ingrese el monto y al finalizar presione 0: "))
    sumaMontos = 0
    cantidad = 0
    while montos != 0:
        montos = float(input("ingrese el monto y al finalizar presione 0: "))
        sumaMontos = sumaMontos + montos
        cantidad = cantidad + 1
    promedioTotal= sumaMontos / cantidad
    print(f"""se vendieron {cantidad} articulos.
el total de venta es igual a : {sumaMontos}
el promedio es de {promedioTotal}""")

montos()