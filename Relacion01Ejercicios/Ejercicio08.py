#Dise�a un programa que solicite la lectura de un n�mero entre 0 y 10 (ambos
#inclusive). Si el usuario teclea un n�mero fuera del rango v�lido, el programa
#solicitar� nuevamente la introducci�n del valor cuantas veces sea necesario.

n = int(input("Escribe un numero de 0 a 10:  "))

while(n < 0 or n > 10):
	n = int(input("Escribe un numero de 0 a 10:  "))