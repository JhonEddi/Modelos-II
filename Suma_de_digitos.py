>>> def sumdigitos(n):
	if n/10==0:
		return n;
	if n/10!=0:
		return n%10+sumdigitos(int(n/10))
