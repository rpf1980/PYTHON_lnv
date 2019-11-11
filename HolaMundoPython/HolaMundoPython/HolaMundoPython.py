print("Hola Mundo")

nEntero = 23
print(nEntero)
strString = "Carlos"
print(strString)

# Declaro variable de tipo números complejos
numeroComplejo = 3+5j
print(numeroComplejo)

# Declaro variable de tipo octal

# Declaro variable de tipo hexadecimal

# Muestra tipo del valor de la variable
print(type(nEntero)) 
print(type(strString))
print(type(numeroComplejo))

# Podemos cambiar el tipo de valor de una variable en cualquier momento
nEntero = "Pack"
print(nEntero)

# División entera
divEntera = 15 // 2
print(divEntera)

# Exponente
potencia = 3**2
print(potencia)

# Saltos de línea en los strings ( Como el \n )
lineas = """Primera línea 
Segunda línea"""
print(lineas)
			
# COLECCIONES:

	#LISTAS:
lista = [22, True, "una línea", [1,2,3,4,5]]
print(lista)

	#Accedemos a sus elementos
valorElementoList = lista[0]
print(valorElementoList)

	#Acceder a elementos de una lista dentro de nuestra lista original
	#Primero accedemos al elemento/posición de la lista y luego a sus propios elementos
valorListaEnLista = lista[3][4]
print(valorListaEnLista)

	#Acceder a elementos de la lista partiendo desde el final ( como length - 2 o length - 1 , etc..etc...)
print(lista[-3])

	# Slicing o particionado ( como el substring() )
fragmentoLista = lista[0:2]
print(fragmentoLista)
fragmentoLista = lista[0:3:2]
print(fragmentoLista)

	#TUPLAS:
	#La tupla la define realmente la coma, no los paréntesis
	#Las tuplas no pueden modificarse ... son inmutables ( Tamaño y valores fijos desde su construcción )
tupla = (1, 2, True, "python", [3,4,5])
print(tupla[3])
print(tupla[4])

# SECUENCIA DE CARACTERES
c = "hola mundo"
print(c)

print(c[0])
print(c[5:])
print(c[::3])

	# DICCIONARIOS:
	# IMPORTANTE --> Se construye muy parecido alo json.. Clave:Valor
	# La clave es inmutable ( queda registrada en memoria ) y se usa para acceder a los datos
	# La clave admite cualquier tipo de dato menos LISTA y DICCIONARIOS
d = {"Love Actually": "Richard Curtis",
     "Kill Bill": "Tarantino",
	 "Amélie": "Jean-Pierre Jeunet"}
print(d)
print(d["Kill Bill"])

# SENTENCIAS CONDICIONALES
	
	#IF
fav = "mundogeek.net"

if fav == "mundogeek.net":
	print("Tienes buen gusto")

	# if elif else
animal = input("Introduce un animal: ")
# animal =(int)input("Introduce un animal: ") --> int para hacer casting
var = "perro"
if animal == "perro":
	print("Guay!!!")
elif animal == "gato":
	print("Miau !!!")
else:
	print("No es perro ni gato")

	# WHILE
edad = 0
while edad < 18:
    edad = edad + 1
    print("Felicidades, tienes" + str(edad))

	# FOR
secuencia = ["uno","dos","tre"]

for elemento in secuencia:
	print(elemento)

# FUNCIONES

def mostrar_datos(param = "Hola", param2 = 300):
	print(param)
	print(param2)

mostrar_datos()
