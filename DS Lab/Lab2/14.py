l=[11, -21, -30, 45,66, -93,99]
l2=[]
for i in range(len(l)):
    if(l[i]%2):
        l2.append(l[i])
print(l)
l=l2
print(l)