>>> def mayorDigito(n):
	if n<=9:
		return n
	if (n%10 < n%100/10):
		return mayorDigito(int(str(n)[:-1]))
	if (n%10 > n%100/10):
		return mayorDigito(int(str(n)[:-2]+str(n)[-1]))
