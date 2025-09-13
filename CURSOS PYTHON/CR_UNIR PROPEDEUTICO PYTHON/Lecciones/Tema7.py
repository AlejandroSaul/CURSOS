import numpy as np
import sys #Para preguntar por memoria
import time

lista = range(1000)
array = np.array(range(1000))

#print(sys.getsizeof(1)*len(lista)) #Calcula lo que ocupa en memoria devuelto en bytes

#print(array.size * array.itemsize) #Calcula lo que ocupa en memoria devuelto en bytes
#los arreglos ocupan menos espacio en memoria

lista1= range(100000)
lista2= range(100000)
array1 = np.array(range(100000))
array2 = np.array(range(100000))

comienzo = time.time()
resultado = [x - y for x,y in zip(lista1,lista2)]
final = time.time()
#print('Tiempo 1 =',final-comienzo)
comienzo2 = time.time()
resultado2 = array1-array2
final2 = time.time()
#print('Tiempo 2 =',final2-comienzo2)

#--------

array1 = np.array([10,20,30])
array2 = np.array([1,2,3])
#print(np.subtract(array1,array2))

#print(np.add(array1,array2))

#print(np.multiply(array1,array2))

#print(np.divide(array1,array2))

#print(np.power(array1,array2))

#print(np.sqrt(array1))

#print(np.square(array1))

#print(np.gcd(array1,array2))

#print(np.lcm(array1,array2))

#print(np.greater(array1,array2))

#print(np.not_equal(array1,array2))

#print(np.logical_and(array1,array2))

print()