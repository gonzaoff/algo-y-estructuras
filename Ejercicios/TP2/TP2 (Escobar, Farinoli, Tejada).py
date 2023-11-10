
import os 

def consumo(ruta_in,ruta_con,codigo,cantidad,motivo,fecha):
    with open(ruta_in) as archivo_insumos:
        contenido_in = archivo_insumos.readlines()
        contenido_in_nuevo = contenido_in
        indi = len(contenido_in)
    #recorremos el archivo
    for i in range(indi):
        #vemos los cod
        cod = int(contenido_in[i].split(";")[0])
        #controlamos el almacen
        almacen = int(contenido_in[i].split(";")[2])
        #controlamos que el codigo corresponda a el producto pedido y el almacen correspondiente
        if (cod == codigo) and (almacen == 1):
            #vemos el stock
            stock_actual = int(contenido_in[i].split(";")[3])
            #controlamos que tenemos stock para retirar 
            if stock_actual >= cantidad:
                #almacenamos en variables datos de la lista 
                name = str(contenido_in[i].split(";")[1])
                precio_costo = contenido_in[i].split(";")[4]
                stock_minimo = contenido_in[i].split(";")[5]
                #resultado de stock 
                stock_resultado = stock_actual - cantidad
                #almacenamos la lista
                contenido_in_nuevo[i] = (f"{cod};{name};{almacen};{stock_resultado};{precio_costo};{stock_minimo}")
                with open(ruta_in,"w") as archivo_insumos:
                    archivo_insumos.writelines(contenido_in_nuevo)
                #registramso el movimiento en consumos.txt
                #codInsumo;Fecha;motivo (1: rotura / 2: posventa / 3: faltante);cantidad ---consumos---
                registo_consumos = (f"{cod};{fecha};{motivo};{cantidad}")
                archivo_consumos = open(ruta_con,"a")
                archivo_consumos.write(registo_consumos)

                return True, print("se logro")
            return False, print("codigo no encontrado o no hay stock suficiente")
    return False, print("no se logro")
                

#almacen insumos 1, almacen terminados 2
def traspaso(ruta_in,ruta_term,codigo,almacen,cantidad):
    # sourcery skip: low-code-quality
    #definimos que almacen trabajaremos
    if almacen == 1 :
        ruta = ruta_in
        almacen_origen = 1
        almacen_destino = 2
    else:
        ruta = ruta_term
        almacen_origen = 2
        almacen_destino = 3

    with open(ruta) as mi_archivo:
        contenido = mi_archivo.readlines()
        lineas = len(contenido)

    cambio = False

    #recorremos el archivo
    for i in range(lineas):
        #obtenemos el codigo y almacen 
        cod = int(contenido[i].split(";")[0])
        almacen_lista = int(contenido[i].split(";")[2])
        #controlamos el stock
        stock_insumos_actual = int(contenido[i].split(";")[3])

        if (cod == codigo) and (almacen_lista == almacen_origen) and (stock_insumos_actual >= cantidad):

            cambio = True
            #restamos el stock del producto de insumos
            stock_insumos = stock_insumos_actual - cantidad

            #almacenamos las variables con los otros datos 
            name = contenido[i].split(";")[1]
            if almacen == 1:
                precio_costo = contenido[i].split(";")[4]
                stock_minimo = contenido[i].split(";")[5]

                #almacenamos el nuevo stock de insumos 

                lista_nueva = (f"{cod};{name};{almacen_origen};{stock_insumos};{precio_costo};{stock_minimo}")
            else:
                lista_nueva = (f"{cod};{name};{almacen_origen};{stock_insumos}\n")
            contenido[i]= lista_nueva
            with open(ruta,"w") as mi_archivo:
                mi_archivo.writelines(contenido)
        if (cod == codigo) and (almacen_lista == almacen_destino) and (cambio == True):

            #sumamos el stock en el nuevo almacen 
            stock_insumos = stock_insumos_actual + cantidad

            #almacenamos las variables con los otros datos 
            name = contenido[i].split(";")[1]
            if almacen == 1:
                precio_costo = contenido[i].split(";")[4]
                stock_minimo = contenido[i].split(";")[5]

                #almacenamos el nuevo stock de insumos 

                lista_nueva = (f"{cod};{name};{almacen_destino};{stock_insumos};{precio_costo};{stock_minimo}")
            else:
                lista_nueva = (f"{cod};{name};{almacen_destino};{stock_insumos}\n")
            contenido[i]= lista_nueva
            with open(ruta,"w") as mi_archivo:
                mi_archivo.writelines(contenido)
            return True, print("cambios realizados")

    return False


def stock(ruta_ins, ruta_term, almacen):
    # Evaluamos el almacen del cual se desea realizar el control de stock
    ruta = ruta_ins if almacen in ["insumos", "1", "INSUMOS"] else ruta_term

    with open(ruta) as archivo:
        contenido = archivo.readlines()

    nuevo_contenido = []

    for linea in contenido:
        # Almacenamos en variables los datos de la línea
        datos = linea.split(";")
        if len(datos) >= 4:
            stock = int(datos[3])

            # Verificamos que solo sean productos con stock positivo
            if stock > 0:
                cod = datos[0]
                name = datos[1]
                alm = datos[2]
                # Creamos la línea nueva
                nueva_linea = f"{cod};{name};{alm};{stock}"
                print(nueva_linea)

    return True



############################################################################################################
#                """AGREGAR RUTAS DE ARCHIVOS TXT """
############################################################################################################
ruta_insumos = "/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/insumos.txt"
ruta_termiandos = "/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/terminados.txt"
ruta_consumos = "/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/TP2/consumos.txt"


## GENERAMOS EL MENU

print("------ Menu de Gestion Movimientos --------")
num_usuario = int(input("Gestion de movimientos [1], Reporte de stock [2], salir [0]: "))

while num_usuario < 0 or num_usuario > 2:
    print("El numero ingresado no es correcto.")
    num_usuario = int(input("Gestion de movimientos [1], Reporte de stock [2], salir [0]: "))


while num_usuario in {1, 2}:
    
    if num_usuario == 1:
        print("---Gestion de movimientos---")
        accion = int(input("Desea controlar un consumo [1], o un traspaso [2] :"))
        while accion < 1 or accion > 2:
            print("El numero ingresado no es correcto") 
            accion = int(input("Desea controlar un consumo [1], o un traspaso [2] :"))

        codigo = int(input("Ingrese el codigo del producto: "))
        if accion == 1:
            cantidad = int (input("Ingrese la cantidad del producto a consumir:  "))
            motivo = str(input("Ingrese el motivo del consumo (1: rotura / 2: posventa / 3: faltante): "))
            fecha = input("Ingrese la fecha de la siguiente forma dd/mm/aaaa: ")

            consumo (ruta_insumos,ruta_consumos,codigo,cantidad,motivo,fecha)
        else:
            almacen = int(input("Ingresae el almacen  insumos (1), almacen terminados (2): "))
            cantidad = int (input("Ingrese la cantidad del producto a traspasar:  "))

            traspaso(ruta_insumos,ruta_termiandos,codigo,almacen,cantidad)

    else:
        print("---Reporte de Stock---")
        almacen = input("almacen 1 (insumos) o almacen 2 (terminados): ")

        stock(ruta_insumos,ruta_termiandos,almacen)
    

    num_usuario = int(input("Gestion de movimientos [1], Reporte de stock [2], salir [0]: "))
        
        