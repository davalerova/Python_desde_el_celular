list1 = [12, 24, 32, 39, 45, 50, 54]
n = 45

def binary_search(lista, n):
	low = 0
	mid = 0
	high = len(lista) - 1
	
	while low <= high:
		mid = (low + high)//2
		
		if lista[mid] < n:
			low = mid - 1
		elif lista[mid] > n:
			high = mid + 1
		else:
			return mid
	return -1
	
res = binary_search(list1, n)
if res == -1:
	print('Valor no encontrado')
else:
	print('El numero {} se encuentra en el index {}'.format(n, res))