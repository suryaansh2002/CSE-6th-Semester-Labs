
f1 = open("f1.txt","r")
f2 = open("f2.txt","w+")

s=f1.read()
 
print(s[::-1])

f2.write(s[::-1])