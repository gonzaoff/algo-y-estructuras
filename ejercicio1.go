package main

import (
	"fmt"
)

func main() {

	//Objetivo: obtener la liquidacion del sueldo.

	//input:nombreApellido, DNI, sueldoBasico, antiguedad(0,012), falto(monto), conyuge(800), hijos, cantHijos(400)
	//descuentos: apJub(0,11), obSoc(0,03), apGr(0,01)
	//output: nombreApellido, DNI, sueldoNeto, suelCnDesc, suelBn

	//idea: pedir los datos, almacenarlos y presentarlos.
	fmt.Println("Ingrese su nombre y apellido")
	var nombreApellido string
	fmt.Scan(&nombreApellido)

	fmt.Println("Ingrese su DNI.")
	var DNI int
	fmt.Scan(&DNI)

	fmt.Println("Sueldo Basico")
	var sueldoBasico float32
	fmt.Scan(&sueldoBasico)

	fmt.Println("Hace cuantos años trabaja: ")
	var antiguedad float32
	fmt.Scan(&antiguedad)

	bonifAnt := antiguedad * (0.12)

	fmt.Println("Le corresponde de antiguedad: ", bonifAnt)

	fmt.Println("Tuvo faltas este mes?(S o N)")
	var presentismo string
	fmt.Scan(&presentismo)

	var valPresentismo float32 = 0

	if presentismo == "N" {
		valPresentismo = 400
		fmt.Println("Le corresponde de presentismo", valPresentismo)
	} else {
		valPresentismo = 0
		fmt.Println("Le corresponde de presentismo", valPresentismo)
	}

	fmt.Println("Tiene conyuge? (S o N)")
	var conyuge string
	fmt.Scan(&conyuge)

	var valConyu float32 = 0

	if conyuge == "S" {
		valConyu = 800
		fmt.Println("Le corresponde de conyuge", valConyu)
	} else {
		valConyu = 0
		fmt.Println("Le corresponde de conyuge", valConyu)
	}

	fmt.Println("Tiene hijos? (S o N)")
	var hijos string
	fmt.Scan(&hijos)

	var cantHijos float32 = 0
	var bonifXHijo float32 = 0

	if hijos == "S" {
		fmt.Println("Cuantos hijos tiene?")
		fmt.Scan(&cantHijos)
		if cantHijos != 0 {
			bonifXHijo = cantHijos * 400
			fmt.Println("Le corresponde de hijos", bonifXHijo)
		} else {
			bonifXHijo = 0
			fmt.Println("Le corresponde de hijos", bonifXHijo)
		}
	}
	sumaAnt := sueldoBasico * bonifAnt
	bonif := sueldoBasico + valPresentismo + valConyu + bonifXHijo + sumaAnt

	var apJub float32 = 0.11
	var obSoc float32 = 0.03
	var apGr float32 = 0.01

	suelDesc := sueldoBasico * (apJub + obSoc + apGr)
	suelBasDes := sueldoBasico - suelDesc

	fmt.Println("La liquidacion de sueldo para", nombreApellido, "DNI: ", DNI)
	fmt.Println("el sueldo neto es: $", int(sueldoBasico))
	fmt.Println("el sueldo con descuentos es: $", int(suelBasDes))
	fmt.Println("el sueldo bonificado es: $", int(bonif)-int(suelBasDes))

	// precioViajes()
	// intercambio()
	// cambioVal()
	// areaYPerimetro()
}

func intercambio() {
	fmt.Println("Ingresa un valor numerico: ")

	var input int
	fmt.Scan(&input)

	result := input * 2

	fmt.Println("el resultado es ", result)
}

func cambioVal() {
	fmt.Println("Ingresa un valor Inicial: ")
	var A int
	fmt.Scan(&A)

	B := 2

	aux := 0

	aux = A

	A = B

	B = aux

	fmt.Println("A es", A, "B es", B, "aux es", aux)

}

func areaYPerimetro() {
	//Area y perimetro de un circulo.
	pi := 3.1416

	fmt.Println("Ingresa el radio del circulo: ")

	var radio float64
	fmt.Scan(&radio)

	fmt.Println("El area del circulo es: ", pi*radio*radio)

	fmt.Println("El perimetro del circulo es: ", 2*pi*radio)
}

func precioViajes() {

	//input: kmInicio, kmFinal, KMxL, precioCombustible
	//output: precioViaje

	fmt.Println("Ingrese el valor inicial del odometro. ")
	var kmInicio int
	fmt.Scan(&kmInicio)

	fmt.Println("Ingrese el valor final del odometro. ")
	var kmFinal int
	fmt.Scan(&kmFinal)

	const KMxL int = 11

	fmt.Println("Ingrese el precio del combustible. ")
	var precioCombustible float32
	fmt.Scan(&precioCombustible)

	var recorrido int = kmFinal - kmInicio
	fmt.Println("Se recorrieron:", recorrido)

	var nafta int = recorrido / KMxL
	fmt.Println("Los litros de nafta consumidos son: ", nafta)

	var precioViaje int = nafta * int(precioCombustible)
	fmt.Println("el viaje sale: $", precioViaje)
}
