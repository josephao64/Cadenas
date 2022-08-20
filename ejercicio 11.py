producto = input('ingrese el nombre del producto: ')
precio = float(input('ingrese el precio por unidad: '))
unidades = int(input('ingrese el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}Q = {total:11.2f}Q'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
