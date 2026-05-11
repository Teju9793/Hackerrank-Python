import numpy
n=int(input())
a=numpy.array([list(map(float,input().split())) for i in range(n)])
print(numpy.linalg.det(a))
