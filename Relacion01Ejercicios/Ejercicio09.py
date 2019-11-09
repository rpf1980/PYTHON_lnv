#Realiza un programa que proporcione el desglose en billetes y monedas de una
#cantidad entera de euros. Recuerda que hay billetes de 500, 200, 100, 50, 20, 10 y
#5 euros y monedas de 2 y 1 euros. Debes recorrer los valores de billete y moneda
#disponibles con uno o mas bucles for-in.

cantidadEntera = float(input("Escribe cantidad de euros:"))

cambio = cantidadEntera - 1000

if(cambio >= 1000):
	cambio = cambio - 1000
	print("2 billetes de 500 euros")
elif(cambio >= 500):
	cambio = cambio - 500
	print("1 billete de 500 euros")
elif(cambio >= 400):
	cambio = cambio -400
	print("2 billetes de 200 euros")
elif(cambio >= 200):
	print("1 billetes de 200 euros")
elif(cambio >= 100):
	cambio = cambio - 100
	print("1 billetes de 100 euros")
elif(cambio >= 50):
	cambio = cambio - 50
	print("1 billete de 50 euros")
elif(cambio >= 40):
	cambio = cambio - 40
	print("2 billetes de 20 euros")
elif(cambio >= 20):
	cambio = cambio - 20
	print("1 billete de 20 euros")
elif(cambio >= 10):
	cambio = cambio - 10
	print("1 billete de 10 euros")
elif(cambio >= 5):
	cambio = cambio - 5
	print("1 billete de 5 euros")
elif cambio >= 4:
	cambio = cambio - 4
	print("2 monedas de 2 euros")
elif cambio >= 2:
	cambio = cambio - 2
	print("1 moneda de 2 euros")
elif cambio >= 1:
	cambio = cambio - 1
	print("1 moneda de ")
else:
	print("")



