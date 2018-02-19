>>> def cantidadDigitos(n):
	if n<=9:
		return 1
	return 1+cantidadDigitos(n/10)
