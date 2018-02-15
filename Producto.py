>>> def producto(n,m):
	if m==0:
		return 0;
	if m==1:
		return n;
	return n+producto(n,m-1)

