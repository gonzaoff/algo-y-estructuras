import contador as c
insumos="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/insumos.txt"
consumos="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/consumos.txt"
terminados="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/terminados.txt"
OrdenesCompra="/home/gonza-pc/Escritorio/cursoprogram/algo-y-estructuras/Ejercicios/OrdenesCompra.txt"

def consumo(cod,cantidad,motivo):
    with open(consumos)