Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sumdigitos(n):
	if n/10==0:
		return n;
	if n/10!=0:
		return n%10+sumdigitos(int(n/10))

	
>>> print (sumdigitos(54178))
25
>>> 
