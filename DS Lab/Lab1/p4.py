import numpy as np
for val in [5,4,3,2,1]:
    print(val)
print ('Done')


stud=['Ram','Vijay','Nithya','Anu','Ramesh','suja']
for k in stud:
    print('Hello:', k)
print('done')


for i in range(5):
    print(i)
    if i>2:
        print('Bigger than 2')
    print('Done with i',i)



x=int(input('Enter a number:'))
for i in range(1,x+1):
    if x%i ==0:
        print(i)
x=10


from math import *
x= [9, 41, 12, 3, 74, 15]
Largest=-inf
for i in x:
    if i>Largest:
        Largest=i
print(Largest)


from math import *
x= [9, 41, 12, 3, 74, 15]
smallest=inf
for i in x:
    if i<smallest:
        smallest=i
print(smallest)


x= [9, 41, 12, 3, 74, 15]
count=sum=avg=0
for i in x:
    count=count+1
    sum=sum+1
avg=sum/count
print(count)
print(sum)
print(avg)


x= [9, 41, 12, 3, 74, 15]
for i in x:
    if i>20:
        print (i)


x= [9, 41, 12, 3, 74, 15]
res=[]
for i in x:
    if i>20:
        res.append(i)

y=np.zeros(len(x))
for i in range(len(x)):
    if x[i]>20:
        y[i]=x[i]
print(y)