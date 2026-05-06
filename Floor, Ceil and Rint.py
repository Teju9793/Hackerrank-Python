import numpy as np

np.set_printoptions(legacy='1.13')

n = np.array(list(map(float, input().split())))

print(np.floor(n))
print(np.ceil(n))
print(np.rint(n))
