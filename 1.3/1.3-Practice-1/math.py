first_number = int(input("Enter a number: "))
next_number = int(input("Enter another number: "))

math = input("+ or - these numbers?: ")
if math == "+":
    print(first_number + next_number)
elif math == "-":
    print(first_number - next_number)
else:
    print("Unknown operator")
