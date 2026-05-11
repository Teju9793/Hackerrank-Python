import numpy as np
co= list(map(float,input().split()))
val=int(input())
r=np.polyval(co,val)
print(r)
