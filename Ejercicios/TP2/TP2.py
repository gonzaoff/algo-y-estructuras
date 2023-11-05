import contador as c
insumos="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/insumos.txt"
consumos="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/consumos.txt"
terminados="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/terminados.txt"
OrdenesCompra="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/OrdenesCompra.txt"

def consumo(ruta1,ruta2,codBuscado,fecha,motivo,cantidad):
    
    
    
    with open(ruta1) as archivo:
        contenido=archivo.readline()
    
    filas=len(contenido)
    
    for i in range(filas):
        cod = int(contenido[i].split(";")[0])
        
        if cod == codBuscado:
            c.stocker(ruta1,codBuscado)
            c.agregarArt(ruta1,fecha,motivo,cantidad)
            
            with open(ruta2) as archivo:
                contenido=archivo.readlines()

                filas = len(contenido)

                for i in range(filas):
                    cod = int(contenido[i].split(";")[0])

                    if cod == codBuscado:
                        nombre = str(contenido[i].split(";")[1])
                        almacen = int(contenido[i].split(";")[2])
                        stock = int(contenido[i].split(";")[3])
                        precioCosto = int(contenido[i].split(";")[4])
                        stockMin = int(contenido[i].split(";")[5])
                        stockConsumo = stock - cantidad
                        stockProd = stock + cantidad
                        
                        if almacen == 1:
                            contenido[i] = f"{cod};{nombre};{almacen};{stockConsumo};{precioCosto};{stockMin}\n"
                        elif almacen == 2:
                            contenido[i] = f"{cod};{nombre};{almacen};{stockProd};{precioCosto};{stockMin}\n"
                            
                        with open(ruta2, "w") as modifica:
                            modifica.write("".join(contenido))

consumo(consumos,insumos,1,"23/03/01",1,13)