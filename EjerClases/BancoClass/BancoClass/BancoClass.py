class Cuenta:
	numCuenta = 0
	dni = ""
	saldo = 0.0
	interes = 0.0

	def __init__(self, dni, saldo, interes):
		self.dni = dni
		self.saldo = saldo
		self.interes = interes

	def actualizar_saldo(self):
		
		self.saldo = self.saldo * (1 + self.interes / 365)
		return self.saldo

	def ingresar(self, ingreso):

		self.saldo = self.saldo + ingreso
		return self.saldo

	def retirar(self, cantidad):

		if(self.saldo > cantidad):
			self.saldo -= cantidad
		else:
			print("No tiene suficiente saldo")
		return self.saldo 

	def mostrar_datos(self):
				
		print("CC: " + str(self.numCuenta))
		print("DNI: " + self.dni)
		print("SALDO: " + str(self.saldo))

# PEDIMOS DATOS POR CONSOLA AL USUARIO
print("INGRESA LOS DATOS DEL USUARIO:")
print()

numCc = int(input("CC: "))
numDni = input("DNI: ")
saldoB = float(input("SALDO: "))
inres = float(input("INTERÉS: "))
print()

# Instanciamos la clase
c = Cuenta(numDni, saldoB, inres)

print("Test función actualizar_saldo():")
print(c.actualizar_saldo())
print()

print("Test función ingresar():")
print()
cantidadIngresas = float(input("Ingrese cantidad de efectivo: "))
print(str(c.ingresar(cantidadIngresas)))
print()

print("Test función retirar():")
print()
cantidadRetiras = float(input(""))
print(str(c.retirar(cantidadRetiras)))
print()

print("Test función mostrar_datos():")
print(str(c.numCuenta()))
print(str(c.mostrar_datos()))
