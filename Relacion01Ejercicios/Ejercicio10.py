#Escribe un programa que resuelva la ecuacion de segundo grado. Para ello tendras
#que importar la clase math (import math) al comienzo del programa, y usar la
#funcion sqrt de dicha clase. Tienes que controlar todos los posibles errores que
#pueden ocurrir.

import math

a = float(input("Escribe el valor de A: ")) # a = cociente del termino cuadrático
b = float(input("Escribe el valor de B: ")) # b = cociente de termino lineal
c = float(input("Escribe el valor de C: ")) # c = cociente de termino independiente

x = (b**2)-(4*a*c)

if x < 0:
    print("Solucion solo en numeros complejos")

x1 = (-b + math.sqrt(x)) / (2*a)
x2 = (-b - math.sqrt(x)) / (2*a)

print("X1: ", x1)
print("X2: ", x2)

