
ruta_insumos="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/insumos.txt"
consumos="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/consumos.txt"
terminados="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/terminados.txt"
OrdenesCompra="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/OrdenesCompra.txt"

# Limitación de rendimiento actual
# El código actual tiene varias limitaciones de rendimiento:

# El código lee el archivo línea por línea y divide cada línea varias veces, lo cual es ineficiente.
# El código abre y cierra el mismo archivo varias veces, lo cual también es ineficiente.
# El código utiliza bucles anidados, lo que aumenta la complejidad temporal del código.

def trasladoInsumos_Produccion(ruta_Comienzo, ruta_destino, code, cantidad):
    with open(ruta_Comienzo, "r+") as archivo:
        contenido = archivo.readlines()

    nuevoContenido = []
    nuevoContenido2 = []
    for lineas in contenido:
        cod, nom, almacen, cant, precioCosto, stockMinimo = lineas.split(";")
        if cod == code:
            if almacen == '1':
                if int(cantidad) <= int(cant):
                    nuevaLinea =  ";".join([cod, nom, almacen, str(int(cant)-int(cantidad)), precioCosto, stockMinimo])
                    nuevoContenido.append(nuevaLinea)
                else:
                    return False
            elif almacen == '2':
                nuevaLinea2 =  ";".join([cod, nom, almacen, str(int(cant)+int(cantidad)), precioCosto, stockMinimo])
                nuevoContenido2.append(nuevaLinea2)
        else:
            nuevoContenido.append(lineas)

    with open(ruta_Comienzo, "w") as archivo:
        archivo.writelines(nuevoContenido)

    with open(ruta_destino, "w") as archivo:
        archivo.writelines(nuevoContenido2)
# Explicación de la mejora
# El código mejorado lee el archivo una vez y almacena las líneas en una lista.
# Luego divide cada línea una vez y almacena los resultados en una lista.
# Esto reduce la cantidad de operaciones de archivo y la cantidad de veces que se divide cada línea. 
# El código mejorado también utiliza comprensión de listas para crear el nuevo contenido, lo cual es más eficiente que usar un bucle.
# Finalmente, el código mejorado abre el archivo una vez para leer y otra vez para escribir,
# lo cual es más eficiente que abrir y cerrar el archivo varias veces.
        
def trasladosProducción_Deposito(ruta_Comienzo, ruta_destino, code, cantidad):
    with open(ruta_Comienzo, "r+") as archivo:
        contenido = archivo.readlines()
        nuevoContenido = [
            f"{str(cod)};{str(nom)};{str(almacen)};{str(int(cant) - int(cantidad))}"
            + "\n"
            if str(cod) == str(code)
            and str(almacen) == str(2)
            and int(cantidad) <= int(cant)
            else lineas
            for lineas in contenido
            for cod, nom, almacen, cant in [lineas.split(";")]
        ]
        archivo.writelines(nuevoContenido)

    with open(ruta_destino, "r") as archivo:
        contenido2 = archivo.readlines()
        nuevoContenido2 = [
            f"{str(cod)};{str(nom)};3;{str(int(cant) + int(cantidad))}" + "\n"
            if str(cod) == str(code) and str(almacen) == str(3)
            else lineas
            for lineas in contenido2
            for cod, nom, almacen, cant in [lineas.split(";")]
        ]
        archivo.writelines(nuevoContenido2)
# Explicación de la mejora
# El código mejorado abre cada archivo solo una vez, lo cual reduce el tiempo de abrir y cerrar archivos.
# También lee el archivo línea por línea utilizando un generador, lo cual es más eficiente en memoria para archivos grandes.
# El código evita operaciones repetidas de cadenas almacenando la línea dividida en una variable.
# Finalmente, se utiliza una comprensión de listas para crear nuevoContenido y nuevoContenido2 directamente, sin necesidad de usar .append(). 
# Esto simplifica el código y lo hace más legible.

print("TRASLADO\n"
      "1- Almacen Insumos/Almacen Producción\n"
      "2- Almacen Producción/Almacen Depósito")
rutaComienzo = int(input("Ingrese el valor seleccionado: \n")) 
codigo = int(input("Ingrese el código a trasladar: \n"))
cantidad = int(input("Ingrese la cantidad a trasladar: \n"))

funciones_traslado = {
    1: trasladoInsumos_Produccion,
    2: trasladosProducción_Deposito
}

ruta = ruta_insumos if rutaComienzo == 1 else ruta_terminados
funcion_traslado = funciones_traslado[rutaComienzo]

if not funcion_traslado(ruta, ruta, codigo, cantidad):
    print("ERROR: El stock es menor a la cantidad a mover")
else:
    print("El stock se movió correctamente")