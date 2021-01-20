def faltante(lista):
	for i in range(1,len(lista)):
		if ord(lista[i]) - ord(lista[i-1]) > 1:
			return chr(ord(lista[i])-1)
			
print(faltante(["O","Q","R","S"]))