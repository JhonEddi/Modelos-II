Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def division(n,m):
	if n==0:
		return 0;
	if n!=0:
		return 1+division(n-m,m);
