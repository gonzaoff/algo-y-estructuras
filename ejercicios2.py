from os import system
from math import isqrt
system("cls")

###-----------------------------###
###QUITAR LOS COMENTARIOS DE LAS FUNCIONES PARA COMENZAR A UTILIZARLAS!!##


def Factorial():

    #input: Numero desde 100 hasta 1.000.000
    #output: Factorial del numero.

    numero=int(input("Ingrese el numero (desde 100 hasta 1.000.000) del que desea saber el factorial: "))
    condicion= numero >= 100 and numero <= 1000000

    if condicion:
        factorialPos= numero
        factorialNeg= numero * (-1)
        print(f"""El valor positivo es: {factorialPos}\nEl Valor negativo es: {factorialNeg}""")
    else:
        numero=int(input("Ingrese un valor valido (entre 100 y 1.000.000): "))
    
# Factorial()

def Resolvente(A,B,C):
    #input:valores "A,B,C" que se reemplacen en una resolvente.

    #A=Variable cuadratica
    #B=Variable lineal
    #C=Variable independiente

    #output: resultado de la resolvente.

    x1=int()
    x2=int()
    d1=B**2-(4*A*C)
    d2=B**2-(4*A*C)

    if d1<0 and d2<0:
        d1 = d1*(-1)
        d2 = d2*(-1)
        x1 = -B+isqrt(d1)/(2*A)
        x2 = -B-isqrt(d2)/(2*A)
        print(f"el valor de la raiz x1: -1*{x1}\nel valor de la raiz x2: -1*{x2}")
        print("El valor de las raices pertene a los numeros complejos.")

    elif d1<0:
        d1 = d1*(-1)
        x1 = -B+isqrt(d1)/(2*A)
        x2 = -B-isqrt(d2)/(2*A)
        print(f"el valor de la raiz x1: -1*{x1}\n")
        print("el valor de la raiz x1 pertenece a los numeros complejos.")

    elif d2<0:
        d2 = d2*(-1)
        x1 = -B+isqrt(d1)/(2*A)
        x2 = -B-isqrt(d2)/(2*A)
        print(f"el valor de la raiz x2: -1*{x2}")
        print("el valor de la raiz x1 pertenece a los numeros complejos.")

    elif d1>0 and d2>0:
        x1 = -B+isqrt(d1)/(2*A)
        x2 = -B-isqrt(d2)/(2*A)
        print(f"el valor de la raiz x1: {x1}\nel valor de la raiz x2: {x2}")

Resolvente(-22,7,-3)

