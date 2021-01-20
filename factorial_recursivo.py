import sys
import time
sys.setrecursionlimit(1000000)

def fac(n):
	respuesta = 1
	while n > 1:
		respuesta *= n
		n -= 1
	return respuesta
	
def fact(n):
	if n ==1:
		return 1
	return n * fact(n - 1)
	
	
n = 10000

ini = time.time()
fac(n)
fin = time.time()

print(fin - ini)


ini = time.time()
fact(n)
fin = time.time()

print(fin - ini)
