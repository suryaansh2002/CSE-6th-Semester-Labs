a= int(input("Enter a:"))
b= int(input("Enter b:"))
c= int(input("Enter c:"))

if a>=b and a>=c:
    print(str(a) + " is greatest")

elif b>=a and b>=c:
    print(str(b) + " is greatest")

elif c>=a and c>=b:
    print(str(c) + " is greatest")