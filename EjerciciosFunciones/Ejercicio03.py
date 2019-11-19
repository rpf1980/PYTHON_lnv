#Realiza una funcion llamada relacion(a, b) que a partir de dos numeros que se
#solicitan al usuario, cumpla lo siguiente:
#a) Si el primer numero es mayor que el segundo, debe devolver 1.
#b) Si el primer numero es menor que el segundo, debe devolver -1.
#c) Si ambos n�meros son iguales, debe devolver un 0.

a = int(input("Escribe primer numero: "))
b = int(input("Escribe segundo numero: "))

def relacion(a, b):
	
	if(a > b):
		print(1)
	elif(a < b):
		print(-1)
	else:
		print(0)

print(relacion(a, b))