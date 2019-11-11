#Realiza una funcion llamada area_circulo(radio) que devuelva el area de un circulo
#a partir de un radio que se solicita al usuario.

import math

radio = float(input("Escribe radio: "))

def areaCirculo(radio):
	return math.pi * (radio**2)

print('Area =  %.2f' % areaCirculo(radio))