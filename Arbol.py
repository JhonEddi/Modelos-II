class arbol:
	def __init__(self,valor,izq = None, der = None):
		self.valor = valor
		self.izquierda = izq
		self.derecha = der

	def buscar (valor,arbol):
		if arbol == None:
			return False
		if arbol.valor == valor:
			return True
		if valor > arbol.valor:
			return buscar(valor,arbol.derecha)
		return buscar (valor,arbol.izquierda)
	
	def inorder (arbol):
		if arbol == None:
			return []
		else: 
			return inorder(arbol.izquierda)+[arbol.valor]+inorder(arbol.derecha)
	
	def insertar (valor,arbol):
		if arbol == []:
			return 
		else:
			return insertar(arbol.izquierda)+[arbol.valor]+inorder(arbol.derecha)