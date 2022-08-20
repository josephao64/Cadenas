precio = input("ingrese el  el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'quetzales y', precio[precio.find('.')+1:], 'céntavos.')
