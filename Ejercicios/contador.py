def maxCod(ruta):
    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)

    maxCod = 0
    for i in range(filas):
        cod = int(contenido[i].split(";")[0])

        if cod > maxCod:
            maxCod = cod

    return maxCod
    
#maxCod(ruta)

def valCod(ruta,valor):
    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)

    for i in range(filas):
        cod = int(contenido[i].split(";")[0])
        if valor == cod:
            return f"{i+1}"
            
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

def precios(ruta,valor):
    
    #INPUT: codigo del producto
    #OUTPUT: stock del producto

    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)
    precio = int()

    for i in range(filas):
        cod = int(contenido[i].split(";")[0])

        if valor == cod:
            return float(contenido[i].split(";")[2])

#precios(ruta,180)

def nombreArt(ruta,codigo):
    
    #INPUT: codigo del producto
    #OUTPUT: stock del producto
    
    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)
    nombre = str()
    
    for i in range(filas):
        cod = int(contenido[i].split(";")[0])
        
        if codigo == cod:
            return str(contenido[i].split(";")[1])
            #print(f"Del codigo {cod} posee un nombre de {nombre}.")
#nombreArt(ruta,180)

def agregarArt(ruta,nombre,precio,stock):
    with open(ruta) as archivo:
        contenido=archivo.readlines()
        
    with open(ruta,"a") as archivo:
        filas = len(contenido)
        for i in range(filas):
            cod = int(contenido[i].split(";")[0])
        escribir = archivo.write(f"{cod+1};{nombre};{precio};{stock}\n")

#nombreArt(ruta,"nuevoArt7",345.76,10)

def consumir(ruta,codBuscado,consumo):

    #INPUT: archivo, codigo y cantidad a consumir.
    #OUTPUT: si la cantidad de stock es igual o menor a la cantidad a consumir.

    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)

    for i in range(filas):
        cod = int(contenido[i].split(";")[0])

        if cod == codBuscado:
            nombre = str(contenido[i].split(";")[1])
            stock = int(contenido[i].split(";")[3])
            precio = float(contenido[i].split(";")[2])
            stockNuevo = stock - consumo
            contenido[i] = f"{cod};{nombre};{precio};{stockNuevo}"
            
            with open(ruta, "w") as modifica:
                modifica.write("".join(contenido))
                
            return stockNuevo

#consumoArt(ruta,180,132)

def modifPrecio(ruta,codBuscado,precioNuevo):

    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)

    for i in range(filas):
        cod = int(contenido[i].split(";")[0])

        if cod == codBuscado:
            nombre = str(contenido[i].split(";")[1])
            stock = int(contenido[i].split(";")[3])
            contenido[i] = f"{cod};{nombre};{precioNuevo};{stock}"
            
            with open(ruta, "w") as modifica:
                modifica.write("".join(contenido))
        
#modifPrecio(ruta,180,203.4)

def modfiStock(ruta,codBuscado,stockNuevo):
    with open(ruta) as archivo:
        contenido=archivo.readlines()

    filas = len(contenido)

    for i in range(filas):
        cod = int(contenido[i].split(";")[0])

        if cod == codBuscado:
            nombre = str(contenido[i].split(";")[1])
            precio = float(contenido[i].split(";")[2])
            contenido[i] = f"{cod};{nombre};{precio};{stockNuevo}"
            
            with open(ruta, "w") as modifica:
                modifica.write("".join(contenido))
#modfiStock(ruta,180,10)