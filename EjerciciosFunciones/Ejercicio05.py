#Realiza una funcion llamada recortar(numero, m�nimo, m�ximo) que reciba tres
#par�metros. El primero es el n�mero a recortar, el segundo es el l�mite inferior y el
#tercero el l�mite superior. La funci�n tendr� que cumplir lo siguiente:
# a) Devolver el l�mite inferior si el n�mero es menor que �ste.
# b) Devolver el l�mite superior si el n�mero es mayor que �ste.
# c) Devolver el n�mero sin cambios si no se supera ning�n l�mite.
# d) Dichos par�metros se solicitan al usuario.

numero = int(input("Escribe un número: "))
minimo = int(input("Escribe número para el líminte inferior: "))
maximo = int(input("Escribe número para el líminte superior: "))
def recortar(numero, maximo, minimo):

	if(numero < minimo):
		print(minimo)
	elif(numero > maximo):
		print(maximo)
	else:
		print(numero)

print(str(recortar(numero, maximo, minimo)))