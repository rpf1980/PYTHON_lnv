class Cuenta:
	numCuenta = 232454000034534000
	dni = "23232323F"
	saldo = 23454.45
	interes = 4.3

	def __init__(self, saldo, interes):
		self.saldo = saldo
		self.interes = interes

	def actualizar_saldo(self):

		self.saldo = interes / 365
		return saldo

	def ingresar(self, ingreso):

		self.saldo += ingreso
		return self.saldo

	def retirar(self, cantidad):

		if(self.saldo < self.cantidad):
			self.saldo -= self.cantidad
		return self.cantidad

	def mostrar_datos(self):
		
		cuenta = Cuenta(2300, 4)
		
		print(str(cuenta.numCuenta))
		print(cuenta.dni)
		print(str(cuenta.saldo))
		print(str(cuenta.interes))
		print(str(cuenta.actualizar_saldo()))
		print(str(cuenta.ingresar(1500)))
		print(str(cuenta.retirar(388.34)))


print(mostrar_datos())