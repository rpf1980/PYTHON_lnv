class Instrumento:
	"""Herencia Python"""
	def __init__(self, precio):
		self.precio = precio

	def tocar(self):
		print("Estamos tocando...")
	def romper(self):
		print("Tu lo has roto. Tienes que pagar "+str(self.precio)+" euros")

class Guitarra(Instrumento, tipoCuerda):
	def __init__(self, tipoCuerda):
		Instrumento.__init__(self, tipoCuerda)
		self.tipoCuerda = tipoCuerda
		print("Tengo una guitarra que vale " + str(self.precio) + " y una cuerda que mide " + self.tipoCuerda)

i = Instrumento(80)
i.tocar()
i.romper()
g = Guitarra(100, "Nylon")
g.tocar()
g.romper()