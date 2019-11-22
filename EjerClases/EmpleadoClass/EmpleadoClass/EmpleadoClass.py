class Empleado:
	nif = ""
	sueldoBase = 0.0	
	pago_hora_extra = 0.0
	h_extras_mes = 0.0
	irpf = 0.0
	casado = False
	num_hijos = 0

	def __init__(self, nif, sueldoBase, pago_hora_extra, h_extras_mes, irpf, casado, num_hijos):

		self.nif = nif
		self.sueldoBase = sueldoBase
		self.pago_hora_extra = pago_hora_extra
		self.h_extras_mes = h_extras_mes
		self.irpf = irpf
		self.casado = casado
		self.num_hijos = num_hijos

	def devoComplementoHorasExtras(self):
		res = self.pago_hora_extra * self.h_extras_mes
		return res

	def devSueldoBruto(self):
		res = self.sueldoBase + self.h_extras_mes
		return res

	def infoEmpleado(self):
		print("NIF: "							  + self.nif)
		print("Sueldo base: "					  + str(self.sueldoBase))
		print("Pago por hora extra: "			  + str(self.pago_hora_extra))
		print("Cantidad de horas extras al mes: " + str(self.h_extras_mes))
		print("IRPF: "							  + str(self.irpf))
		print("Casado: "						  + str(self.casado))
		print("Número de hijos: "				  + str(self.num_hijos))
	
print("ESCRIBA LOS DATOS PARA EL USUARIO (Presione Enter)")

dni = input("DNI: ")
jornalBase = float(input("SUELDO BASE: "))
pagoHorasExtras = float(input("PAGO POR HORA EXTRA: "))
horasExtrasMes = float(input("TOTAL HORAS EXTRAS MES: "))
datoIrpf = float(input("IRPF: "))
estadoCivil = input("CASADO: ")
numeroHijos = int(input("Nº HIJOS: "))

emple = Empleado(dni, jornalBase, pagoHorasExtras, horasExtrasMes, datoIrpf, estadoCivil, numeroHijos)
print()
print("COMPLEMENTO HORAS EXTRAS:")
print(emple.devoComplementoHorasExtras())
print()
print("CÁLCULO Y DEVOLUCIÓN DEL SUELDO BRUTO:")
print(emple.devSueldoBruto())
print()
print("INFORMACIÓN GENERAL DEL EMPLEADO:")
print(emple.infoEmpleado())