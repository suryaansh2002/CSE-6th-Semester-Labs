import numpy as np

a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print(b)

c = a-b
print(c)

print(b**2)
print(10*np.sin(a))

print(a<35)

A = np.array( [[1,1],[0,1]] )
B = np.array( [[2,0],[3,4]] )

print(A*B)
print(A.dot(B))
print(np.dot(A,B))

b = np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0))
print(b.sum(axis=1))

a = np.arange(10)**3
print(a)

print(a[2:5])
print(a[0:6:2])

b=np.array([[ 0, 1, 2, 3],
[10, 11, 12, 13],
[20, 21, 22, 23],
[30, 31, 32, 33],
[40, 41, 42, 43]])

print(b[2,3])
print(b[0:5,1])
print(b[:5,1])
print(b[:,1])
print(b[-1,:])
print(b[:,-1])

for row in b:
    print (row)

for element in b.flat:
    print (element)