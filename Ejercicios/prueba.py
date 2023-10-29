from os import system
system("cls")

numero=12321
variable=str(numero)

comparador1=[]
comparador2=[]

for i in variable:
    comparador1 += i
    
for i in variable[::-1]:
    comparador2 += i
    
if comparador1 == comparador2:
    print("Es capicua")
else:
    print("No es capicua")

