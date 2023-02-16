import numpy as np
import random

A = np.array ([2,5,10])
print(A.dtype)

B=np.array ([2.4,10.6,5.2])
print(B.dtype)

A=np.array([(3,4,5),(12,6,1)])
Z=np.zeros((2,4))
print(A)
print(Z)
S=np.arange(10,30,5)
print(S)
s= np.arange( 0, 2, 0.3 )
print(s)
S1=np.linspace(0,2,9)
print(S1)

print(random.choice([1,2,3,4,5]))
print(random.choice("python"))
print(random.randrange(25,50))
print(random.randrange(25,50,2))
print(random.random())
print(random.uniform(5,10))
random.shuffle([1,2,3,4,5])
random.seed(10)

