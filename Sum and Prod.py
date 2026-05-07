import numpy as np
n,m=list(map(int,input().split()))
a=np.array([list(map(int,input().split())) for _ in range(n)])
s=np.sum(a,axis=0)
print(np.prod(s))
