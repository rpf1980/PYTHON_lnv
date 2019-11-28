""" Escribir una función que aplique un descuento a un precio y otra que aplique el IVA
a un precio. Escribir una tercera función que reciba un diccionario con los precios y
porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice
la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y
devolver el precio final de la cesta. """

#Con esta función obtenemos el precio final después de ser aplicado el IVA que sea a una cantidad dada.
def aplicamosIva(precio, porcentaje):
    return precio + precio * porcentaje / 100

#Con esta función calculamos el precio de los productor de la compra ( cesta compra )