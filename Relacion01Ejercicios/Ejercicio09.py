#Realiza un programa que proporcione el desglose en billetes y monedas de una
#cantidad entera de euros. Recuerda que hay billetes de 500, 200, 100, 50, 20, 10 y
#5 euros y monedas de 2 y 1 euros. Debes recorrer los valores de billete y moneda
#disponibles con uno o mas bucles for-in.

dinero = int(input("Escribe cantidad de euros:"))
billetes = [500, 200, 100, 50, 20, 10, 5]
monedas = [1,2]

for i in billetes:
	n = int(dinero//i)
	if(n<1):
		continue
	else:
		print(str(n) + " billete de " + str(i) + "€")
		dinero = dinero%i

for i in monedas:
	n = int(dinero//i)
	if(n<1):
		continue
	else:
		print(str(n) + "moneda " + str(i) + " € ")
		dinero = dinero%i

