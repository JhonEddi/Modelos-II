Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def producto(n,m):
	if m==0:
		return 0;
	if m==1:
		return n;
	return n+producto(n,m-1)

>>> print (producto(4,3))
12
>>> 
