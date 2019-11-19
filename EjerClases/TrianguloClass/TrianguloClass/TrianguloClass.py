class Triangulo:
	def __init__(self, lado, base, altura):
		self.lado = lado
		self.base = base
		self.altura = altura

	def perimetro(self):
		return (self.lado * self.lado) / self.base

	def area(self):
		return (self.base * self.altura) / 2
	
	def muestra(self):
		mostramos = "Lado: " + str(self.lado) + "\nBase: " + str(self.base) + "\nAltura: " + str(self.altura)
		return mostramos
			 
tri = Triangulo(12,5,23)

print("El perímetro del triángulo es = " + str(tri.perimetro()))
print("El área del triángulo es = " + str(tri.area()))
print("Las propiedades del objeto son:\n" + str(tri.muestra()))

