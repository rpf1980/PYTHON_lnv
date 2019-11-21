class Cuenta:
	numCuenta = 0
	dni = ""
	saldo = 0.0
	interes = 0.0

	def __init__(self, saldo, interes):
		self.saldo = saldo
		self.interes = interes

	def actualizar_saldo(self):

		self.saldo = self.interes / 365
		return self.saldo

	def ingresar(self, ingreso):

		self.saldo += ingreso
		return self.saldo

	def retirar(self, cantidad):

		if(self.saldo > cantidad):
			self.saldo -= cantidad
		return self.saldo #Quieres mostrar lo que queda en cuenta o MOSTRAR la cantidad que hemos retirado ?

	def mostrar_datos(self):
		
		cuenta = Cuenta(2300, 4)
		
		print("CC: " + str(cuenta.numCuenta))
		print("DNI: " + cuenta.dni)
		print("SALDO: " + str(cuenta.saldo))
		print("INTERÉS: " + str(cuenta.interes))
		print("SALDO ACTUALIZADO: " + str(cuenta.actualizar_saldo()))
		print("INGRESO: " + str(cuenta.ingresar(1500)))
		print("RETIRADA EFECTIVO: " + str(cuenta.retirar(388.34)))


cuenta = Cuenta(9999, 0.21)
print(cuenta.mostrar_datos())