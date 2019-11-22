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

		self.saldo += ingreso
		return self.saldo

	def retirar(self, cantidad):

		if(self.saldo > cantidad):
			self.saldo -= cantidad
			res = "Efectivo retirado = " + cantidad + "\n" + "Saldo en cuenta = " + self.saldo 
		return res 

	def mostrar_datos(self):
				
		print("CC: " + str(cuenta.numCuenta))
		print("DNI: " + cuenta.dni)
		print("SALDO: " + str(cuenta.saldo))
		print("INTERÉS: " + str(cuenta.interes))
		print("SALDO ACTUALIZADO: " + str(cuenta.actualizar_saldo()))
		print("INGRESO: " + str(cuenta.ingresar(1500)))
		print("RETIRADA EFECTIVO: " + str(cuenta.retirar(388.34)))

# PEDIMOS DATOS POR CONSOLA AL USUARIO
print("INGRESA LOS DATOS DEL USUARIO:")
print()

numeroCuenta = int(input("CC: "))
numeroDni = input("DNI: ")
cantidadSaldo = float(input("SALDO: "))
interesCuenta = float(input("INTERÉS: "))
print()

# Instanciamos la clase
c = Cuenta(numeroDni, cantidadSaldo, interesCuenta)

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
print(c.retirar())
print()

print("Test función mostrar_datos():")
print(c.mostrar_datos())
print()

