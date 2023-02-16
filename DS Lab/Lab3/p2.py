import numpy as np
import random

a = np.arange(15).reshape(3, 5)
print(a)

print(a.shape)
print(a.T)
print(a.size)

c = np.arange(24).reshape(2,3,4)
print(c)
print(c.shape)
print(c[1,...])
print(c[1,:,:])
