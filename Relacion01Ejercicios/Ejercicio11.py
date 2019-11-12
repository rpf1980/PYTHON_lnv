import math

area = 0.0
opcion = -1

print("==============")
print("CALCULAR AREAS")
print("==============")
print("[1] area de circulo")
print("[2] area de un triangulo")
print("[0] Salir")
print()
opcion = int(input("Elige una opcion: "))

if(opcion == 1):
	radio = float(input("Escribe el radio: "))
	area = math.pi * (radio**2)
	print('area del circulo = %.2f ' % area)

elif(opcion == 2):
	base = float(input("Escribe la base: "))
	altura = float(input("Escribe la altura: "))
	area = (base * altura) / 2
	print('area del triangulo = %.2f' % area)
	