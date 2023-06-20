tabla_desde = 5
tabla_hasta = 9
desde = 1
hasta = 10
for factor1 in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {factor1}:')
	for factor2 in range(desde, hasta + 1):
		print(f'{factor1} x {factor2} = {factor1 * factor2}')
	print()