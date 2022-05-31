import funcion_impuestos

salario = float(input("Ingresa salario" + ' '))
percent = float(input("Ingresa porcentaje de impuestos" + ' '))

result = funcion_impuestos.calcularImpuesto(salario, percent)
print("El total de impuestos sobre el salario es " + str(result))