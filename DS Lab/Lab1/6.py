t=(1,3,5,7,9,2,4,6,8,10)

l=len(t)
for i in range(0, int(l/2)):
    print(t[i], end=" ")

print()
for i in range(int(l/2), l):
    print(t[i], end=" ")
