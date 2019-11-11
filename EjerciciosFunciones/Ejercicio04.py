#Realiza una funcion llamada intermedio(a, b) que a partir de dos numeros, que se
#solicitan al usuario, devuelva su punto intermedio.

a = int(input("Escribe un primer entero: "))
b = int(input("Escribe segundo entero: "))

def intermedio(a, b):
	
	if(a < b):
		intermedio = b // a
	elif(b < a):
		intermedio = a // b
	else:
		print("Los numero son iguales")

		# Error en resultado --------------->
print(intermedio(a, b))