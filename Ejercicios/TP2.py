
ruta="/home/gonza-pc/Escritorio/CursoProgram/algo-y-estructuras/Ejercicios/articulos.txt"


def modifPrecio(ruta,codBuscado,precioNuevo):

    with open(ruta) as archivo:
        contenido=archivo.readlines()

    contenidoNuevo = contenido

    filas = len(contenido)

    codBuscado = int()

    for i in range(filas):
        cod = int(contenido[i].split(";")[0])

        if cod == codBuscado:
            nombre = str(contenido[i].split(";")[1])
            stock = int(contenido[i].split(";")[3])
            lineaNueva = f"{cod};{nombre};{str(precioNuevo)};{stock}"
            contenidoNuevo[i] = lineaNueva

            with open(ruta, "w") as modifica:
                modifica.writelines(contenidoNuevo)
            return True
    
def maxCod(ruta):
    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)

    maxCod = 0
    for i in range(filas):
        cod = int(contenido[i].split(";")[0])

        if cod > maxCod:
            maxCod = cod

    print(maxCod)
    
#maxCod(ruta)

def valCod(ruta,valor):
    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)

    for i in range(filas):
        cod = int(contenido[i].split(";")[0])
        if valor == cod:
            print(f"el codigo {valor} se encuentra en la linea {i+1} de la lista de articulos.")
            
#valCod(ruta,140)

def stocker(ruta,valor):
    
    #INPUT: codigo del producto
    #OUTPUT: stock del producto

    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)
    stock = int()

    for i in range(filas):
        cod = int(contenido[i].split(";")[0])

        if valor == cod:
            return int(contenido[i].split(";")[3])

#stocker(ruta,180)

def precio(ruta,valor):
    
    #INPUT: codigo del producto
    #OUTPUT: stock del producto
    
    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)
    precio = int()
    
    for i in range(filas):
        cod = int(contenido[i].split(";")[0])
        
        if valor == cod:
            precio = float(contenido[i].split(";")[2])
            print(f"Del codigo {cod} posee un precio de {precio}.")

#precio(ruta,180)

def nombreArt(ruta,valor):
    
    #INPUT: codigo del producto
    #OUTPUT: stock del producto
    
    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)
    nombre = str()
    
    for i in range(filas):
        cod = int(contenido[i].split(";")[0])
        
        if valor == cod:
            nombre = str(contenido[i].split(";")[1])
            print(f"Del codigo {cod} posee un nombre de {nombre}.")
#nombreArt(ruta,180)

def nombreArt(ruta,nombre,precio,stock):
    with open(ruta) as archivo:
        contenido=archivo.readlines()
        
    with open(ruta,"a") as archivo:
        filas = len(contenido)
        for i in range(filas):
            cod = int(contenido[i].split(";")[0])
        escribir = archivo.write(f"{cod+1};{nombre};{precio};{stock}\n")

#nombreArt(ruta,"nuevoArt7",345.76,10)

def consumoArt(ruta,codigo,consumo):

    #INPUT: archivo, codigo y cantidad a consumir.
    #OUTPUT: si la cantidad de stock es igual o menor a la cantidad a consumir.

    with open(ruta) as archivo:
        contenido=archivo.readlines()
    
    filas = len(contenido)
    stock = int()
    
    for i in range(filas):
        cod = int(contenido[i].split(";")[0])
        
        if codigo == cod:
            stock = int(contenido[i].split(";")[3])
            
            if consumo <= stock:
                print(f"Hay {stock} existencias, se pueden consumir {consumo} unidades")
            else:ertertertertert
                print("No hay suficiente stock")

consumoArt(ruta,180,132)
    