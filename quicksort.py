import random
def qsort(arr): 
    if len(arr) <= 1:
        return arr
    else:
        return qsort([x for x in arr[1:] if x < arr[0]]) + \
               [arr[0]] + \
               qsort([x for x in arr[1:] if x >= arr[0]])

# this comment is just to improve readability due to horizontal scroll!!!

lista = [random.randint(1,100) for x in range(100) ]

print(lista)
print(qsort(lista))