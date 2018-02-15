Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def fibonacci (n):
	if n<=2:
		return 1;
	if n>2:
		return fibonacci(n-1)+fibonacci(n-2)

	
>>> print (fibonacci(7))
13
>>> print (fibonacci(2))
1
>>> 
