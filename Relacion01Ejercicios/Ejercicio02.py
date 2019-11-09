# Escribe un programa que, a partir de una tupla cualquiera, obtenga una lista con
# todos los elementos de la tupla. Utiliza un bucle.

tupla = (3.5, True, "La casa del arbol", ["perro","gato","loro","pato"])
lista = []

for i in tupla:
	lista.append(i)

print(lista)