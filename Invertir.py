>>> def cantidadDigitos(n):
	if n<=9:
		return 1
	return 1+cantidadDigitos(n/10)

>>> def Invertir(n):
	if  cantidadDigitos(n)==1:
		return n
	if cantidadDigitos(n)!=1:
		return(n%10)*(10**(cantidadDigitos(n)-1))+Invertir(n/10)
