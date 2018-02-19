Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def cantidadDigitos(n):
	if n<=9:
		return 1
	return 1+cantidadDigitos(n/10)
