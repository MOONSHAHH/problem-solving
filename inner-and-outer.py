import numpy
Array1 = numpy.array(input().split(), int)
Array2 = numpy.array(input().split(), int)

print(numpy.inner(Array1, Array2))
print(numpy.outer(Array1, Array2)) 
