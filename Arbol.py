class Arbol:
	def __init__(self,valor,izq = None, der = None):
		self.valor = valor
		self.izquierda = izq
		self.derecha = der
arbol15 = Arbol(10,Arbol(5),Arbol(50,Arbol(30,Arbol(20),Arbol(40))))
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
	if arbol == None:
		return Arbol(valor)
	if valor < arbol.valor:
		return Arbol(arbol.valor,insertar(valor,arbol.izquierda),arbol.derecha)
	if valor > arbol.valor:
		return Arbol(arbol.valor,arbol.izquierda,insertar(valor,arbol.derecha))

