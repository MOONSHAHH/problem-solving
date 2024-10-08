import numpy

N,M,P = int (input().split)

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print (numpy.concatenate((array_1, array_2, array_3))) 