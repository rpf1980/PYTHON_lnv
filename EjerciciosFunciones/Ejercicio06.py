#Realiza una funci�n separar(lista) que tome una lista de n�meros enteros y
#devuelva dos listas ordenadas. La primera con los n�meros pares y la segunda con
#los n�meros impares.

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
listaPares = []
listaImpares = []

def separar(lista):
	
	for i in range(len(lista)):
		if(lista[i] %2 == 0):
			listaPares.append(lista[i])
		else:
			listaImpares.append(lista[i])
	print(listaPares)
	print(listaImpares)

print(str(separar(lista)))
		

