Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def palindromo(n):
	if n<=9 or n<=99:
		if n<=9:
			return "palindromo"
		if int(str(n)[0]) == int(str(n)[1]):
			return "palindromo"
		return "no palindromo"
	if int(str(n)[0]) == int(str(n)[-1]):
		return palindromo(int(str(n)[1:-1]))
	return "no palindromo"
