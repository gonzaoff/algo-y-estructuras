
ruta="C:\\Users\\Gonza\\Desktop\\UNRAF (Actualizado 13-04)\\Segundo Cuatri\\Datos y Estructuras\\Ejercicios\\TP2\\consumos.txt"



def modifPrecio(ruta,codBuscado,precioNuevo):
        # sourcery skip: ensure-file-closed, extract-method
    archivo=open(ruta)

    contenido=archivo.readlines()

    archivo.close()

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

            modifica = open(ruta, "w")
            modifica.writelines(contenidoNuevo)
            modifica.close()
            return True
        
def modifPrecio():