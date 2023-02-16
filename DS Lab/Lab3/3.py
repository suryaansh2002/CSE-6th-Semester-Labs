import numpy as np

l=[1,2,3,4,5]

a=np.array(l, float)
print(a)

t=(1,2,3,4)

b=np.array(t)

print(b)

c=np.zeros((3,4),int)

print(c)

d=np.array(range(0,21,5))

print(d)

e=np.reshape(c,(2,2,3))

print(e)

f=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(f)
print(np.max(f))
print(np.min(f))
print(np.sum(f))

print(np.max(f, axis=1))
print(np.max(f, axis=0))

print(np.min(f, axis=1))
print(np.min(f, axis=0))
