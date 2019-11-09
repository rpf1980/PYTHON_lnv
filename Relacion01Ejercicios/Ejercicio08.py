#Diseña un programa que solicite la lectura de un número entre 0 y 10 (ambos
#inclusive). Si el usuario teclea un número fuera del rango válido, el programa
#solicitará nuevamente la introducción del valor cuantas veces sea necesario.

n = int(input("Escribe un numero de 0 a 10:  "))

while(n < 0 or n > 10):
	n = int(input("Escribe un numero de 0 a 10:  "))