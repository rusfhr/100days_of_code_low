print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

total = 0

if size == "S":
    total += 15
elif size == "M":
    total += 20
else:
    total += 25

if pepperoni == "Y":
    if size == "S":
        total += 2
    else:
        total += 3
else:
    total += 0

if extra_cheese == 'Y':
    total += 1
else:
    total += 0

print('Your final bill is: $' + str(total) + '.')