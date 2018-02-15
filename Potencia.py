>>> def Potencia(n,m):
	if m==0:
		return 1;
	if m>=1:
		return n*potencia(n,m-1)
