import math
class Triangulo:
	def __init__(self, lado, base, altura):
		self.__lado = lado
		self.__base = base
		self.__altura = altura

	#GETTER && SETTER
	def getLado(self):
		return self.__lado
	def setLado(self, lado):
		self.__lado = lado

	def getBase(self):
		return self.__base
	def setBase(self, base):
		self.__base = base

	def getAltura(self):
		return self.__altura
	def setAltura(self, altura):
		self.__altura = altura

	#FUNCIONES
	

	def perimetro(self):
		return (self.__lado + self.__lado) + self.__base

	def area(self):
		return (self.__base * self.__altura) / 2
	
	def muestra(self):
		mostramos = "Lado: " + str(self.__lado) + "\nBase: " + str(self.__base) + "\nAltura: " + str(self.__altura)
		return mostramos

def calculaAltura(a, b):

		return math.sqrt(((a*a) - (b*b)) / 4)
	

# Pedimos datos al usuario
print("==============================================")
print(input("INGRESE LOS DATOS DEL TRIÁNGULO (Presione Enter)"))
print("==============================================")
l = float(input("Lado: "))
b = float(input("Base: "))
a = calculaAltura(l,b)

print()			 
tri = Triangulo(l,b,a)


print("PROBANDO FUNCIONES DE LA CLASE")
print("El perímetro del triángulo es = " + str(tri.perimetro()))
print("El área del triángulo es = " + str(tri.area()))

print()
print("PROPIEDADES DEL OBJETO:\n" + str(tri.muestra()))
print()

print("========================")
print("MÉTODOS GETTER && SETTER")
print("========================")
print("LADO: " + str(tri.getLado()))
print("BASE: " + str(tri.getBase()))
print("ALTURA: " + str(tri.getAltura()))

