from array import *

array1 = array("i", [1,2,3,4,5])

def imp():
	for i in array1:
		print(i)
	
print(array1.index(4))

array1.insert(1,6)
imp()
array1.remove(6)
imp()
print(len(array1))
print(array1[3])