#Realiza una funcion llamada intermedio(a, b) que a partir de dos numeros, que se
#solicitan al usuario, devuelva su punto intermedio.

a = int(input("Escribe un primer entero: "))
b = int(input("Escribe segundo entero: "))

def intermedio(a, b):
	resultado = (a + b) / 2
	return resultado
		# Error en resultado --------------->
print(intermedio(a, b))