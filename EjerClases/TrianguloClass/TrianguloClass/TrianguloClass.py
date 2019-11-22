class Triangulo:
	def __init__(self, lado, base, altura):
		self.lado = lado
		self.base = base
		self.altura = altura

	def perimetro(self):
		return (self.lado + self.lado) + self.base

	def area(self):
		return (self.base * self.altura) / 2
	
	def muestra(self):
		mostramos = "Lado: " + str(self.lado) + "\nBase: " + str(self.base) + "\nAltura: " + str(self.altura)
		return mostramos

# Pedimos datos al usuario
print(input("INGRESE LOS DATOS DEL TRIÁNGULO (Presione Enter)"))
l = float(input("Lado: "))
b = float(input("Base: "))
a = float(input("Altura: "))
print()			 
tri = Triangulo(l,b,a)

print("El perímetro del triángulo es = " + str(tri.perimetro()))
print("El área del triángulo es = " + str(tri.area()))
print()
print("PROPIEDADES DEL OBJETO:\n" + str(tri.muestra()))

