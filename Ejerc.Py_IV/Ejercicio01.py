""" Escribir una función que aplique un descuento a un precio y otra que aplique el IVA
a un precio. Escribir una tercera función que reciba un diccionario con los precios y
porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice
la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y
devolver el precio final de la cesta. """

#Con esta función obtenemos el precio final después de ser aplicado el IVA que sea a una cantidad dada.
def aplicaIvaCalculaPrecio(precio, porcentaje):
    return precio * (porcentaje / 100)

#Con esta función obtenemo precio final de un producto tras aplicarle descuento
def descuentoProducto(precio, desc):
    return precio - desc

#Con esta función calculamos el precio de los productor de la compra ( cesta compra )
def calculaPrecioCompra(diccionario, funCalculos):
    resultado = 0
    for precio, descuento in diccionario.items():
        total = total + funCalculos(precio, descuento)
    return resultado

print("Precio de los productos aplicando IVA = " + calculaPrecioCompra({384:21, 2387:10, 12344:4}, aplicaIvaCalculaPrecio))
print("Precio de los productos con descuento = " + calculaPrecioCompra({384:21, 2387:10, 12344:4}, descuentoProducto))