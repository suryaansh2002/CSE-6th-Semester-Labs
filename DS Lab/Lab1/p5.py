price = 100
if price > 100:
    print("price is greater than 100")
elif price == 100:
    print("price is 100")
elif price < 100:
    print("price is less than 100")

# initialize the variable
i = 1
n = 5
# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

total = 0
number = int(input('Enter a number: '))
# add numbers until number is zero
while number != 0:
    total += number # total = total + number
    # take integer input again
    number = int(input('Enter a number: '))
    print('total =', total)