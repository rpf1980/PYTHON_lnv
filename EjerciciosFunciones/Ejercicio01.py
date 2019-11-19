#Realiza una funcion llamada area_rectangulo(base, altura) que devuelva el area del
#rectangulo a partir de una base y una altura que se solicita al usuario.

base = int(input("Escribe base: "))
altura = int(input("Escribe altura: "))
def areaRectangulo(base, altura):
	return base * altura

print(str("Area = " + str(areaRectangulo(base, altura))))
