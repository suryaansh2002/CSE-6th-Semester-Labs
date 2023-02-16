import numpy as np

b=np.array([[ 0, 1, 2, 3],
[10, 11, 12, 13],
[20, 21, 22, 23],
[30, 31, 32, 33],
[40, 41, 42, 43]])

B1=b.reshape(4,5)
A1=np.array([(3,4,5),(12,6,1)])
A2=np.array([(1,2,6),(-4,3,8)])
D1=np.vstack((A1,A2))
D2=np.hstack((A1,A2))
a = np.array([4.,2.])
b = np.array([3.,8.])
print(np.column_stack((a,b)))
print(np.hstack((a,b)))

a = np.arange(12)**2
i = np.array( [ 1,1,3,8,5 ] )
print(a[i])

j = np.array( [ [ 3, 4], [ 9, 7 ] ] )
print(a[j])

a=np.array([(3,2,9),(1,6,7)])
s1=0
for row in a:
    for col in row:
        s1+=col
print(s1)

s=0
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        s+=a[i,j]
print(s)