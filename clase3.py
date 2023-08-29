class estructuras_algoritmicas():
    def __init__(self):
        self.secuenciales = " Asignacion, entrada, salida"
        self.condicionales = "simples, compuestos, multiples"
        self.ciclicas= "repetis hasta (hacer mietras), mientras, para"
        self.definicon = "definicion del problema(planteamiento)"
        self.conceptualizacion = "Conceptualizacion(...)"
        self.especificacion="especificacion del algoritmo, especificar la secuencia de actividades, dependiendo de la complejidad del algom descomponer en sub-algo"
        self.validacion = "validacion del algoritmo: 1) Dominios - 2)Ejecucion"
        self.limitacion = "Limitaciones del algoritmo: identificacion de puntos debiles (condiciones criticas)"
        self.compilador= ""

class definicion(estructuras_algoritmicas):
    def mostrar_defin(self):
        return f"""estructuras secuenciales: {self.secuenciales}
estructuras condicionales: {self.condicionales}
estructuras ciclicas: {self.ciclicas}
definicion: {self.definicon}
conceptualizacion: {self.conceptualizacion}
espeficacion: {self.especificacion}
validacion: {self.validacion}
limiticion: {self.limitacion}
"""


estructuras=definicion()
print(estructuras.mostrar_defin())
