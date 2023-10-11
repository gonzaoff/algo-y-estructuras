package main

import (
	"fmt"
)

func main() {

	myMap := make(map[int]int)
	myMap[1] = 20
	myMap[3] = 5
	myMap[2] = 10

	fmt.Println(myMap)

	for index := range myMap {
		for value := range myMap {

			total := index * value
			fmt.Println(total)
		}
	}
}

//en un curso de 5 estudiantes se toman 3 parciales. diseñar un algoritmo
//para registrar las notas de los alumnos en una matriz.
// calcular "promedio de cada alumno" y "promedio de cada parcial"
