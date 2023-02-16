l=[11, -21, -30, 45,66, -93,99]
c1=0
c2=0
for i in range(len(l)):
    if(l[i]<0):
        c1+=1
    if(l[i]>0):
        c2+=1

print("Negative:" + str(c1) +" Positive:"+str(c2))