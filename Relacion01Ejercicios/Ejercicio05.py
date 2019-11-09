#Diseña un programa que lea la edad de dos personas y diga quién es más joven, la
#primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En
#tal caso, hazlo saber con un mensaje adecuado.

persona1 = int(input("Edad persona 1:"))
persona2 = int(input("Edad persona 2:"))

if(persona1 > persona2):
	print("La persona 1 es mayor")
elif(persona2 > persona1):
	print("La persona 2 es mayor")
else:
	print("Las edades de las dos personas son las mismas")