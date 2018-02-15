>>> def division(n,m):
	if n==0:
		return 0;
	if n!=0:
		return 1+division(n-m,m);
