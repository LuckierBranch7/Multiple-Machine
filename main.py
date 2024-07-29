x = int(input("Give me a number: "))
l = int(input("How many multiples do you want: "))

def multiples():
    for i in range(l):
        i += 1
        y = x * i
        print(y)

if l <= 1000:
    multiples()
else:
    print("Multiples cannot be more than 1000")