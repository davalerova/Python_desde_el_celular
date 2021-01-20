class Nodo:
	
	def __init__(self, dato_inicial = None):
		self.dato = dato_inicial
		self.siguiente = None
		
	def obtener_dato(self):
		return self.dato
		
	def obtener_siguiente(self):
		return self.siguiente
	
	def asignar_dato(self, nuevo_dato):
		self.dato = nuevo_dato
	
	def asignar_siguiente(self, nuevo_siguiente):
		self.siguiente = nuevo_siguiente
		

class listaNoOrdenada():
		
		def __init__(self):
			self.cabeza = None
		
		def imprimir_lista(self):
			actual = self.cabeza
			while actual is not None:
				print(actual.dato)
				actual = actual.siguiente
			print()
		
		def insertar_al_comienzo(self, dato):
			nuevo_nodo = Nodo(dato)
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo
		
		def insertar_al_final(self, dato):
			nuevo_nodo = Nodo(dato)
			if self.cabeza is None:
				self.cabeza = nuevo_nodo
				return 
			actual = self.cabeza
			while actual.siguiente:
				actual = actual.siguiente
			actual.siguiente = nuevo_nodo
			
		def insertar_en(self, nodo_destino, nuevo_dato):
			if nodo_destino is None:
				print("Nodo vacío")
				return
				
			nuevo_nodo = Nodo(nuevo_dato)
			nuevo_nodo.siguiente = nodo_destino.siguiente
			nodo_destino.siguiente = nuevo_nodo
		
		def eliminar(self, item):
				previo = None
				actual = self.cabeza
				encontrado = False
				
				while not encontrado:
					if actual.dato == item:
						encontrado = True
					else:
						previo = actual
						actual = actual.obtener_siguiente()
					
				if previo is None:
					self.cabeza = actual.obtener_siguiente()
				else:
					previo.asignar_siguiente(actual.obtener_siguiente())
				
				
			
list = listaNoOrdenada()
list.cabeza = Nodo("lunes")

e2 = Nodo("martes")
e3 = Nodo("miercoles")
e4 = Nodo("jueves")
e5 = Nodo("viernes")
list.cabeza.siguiente = e2
e2.siguiente = e3
e3.siguiente = e4
e4.siguiente = e5


list.imprimir_lista()
list.insertar_al_comienzo("domingo")
list.imprimir_lista()
list.insertar_al_final("Sábado")
list.imprimir_lista()

list.insertar_en(e4, "juernes")
list.imprimir_lista()

list.eliminar("juernes")
list.imprimir_lista()