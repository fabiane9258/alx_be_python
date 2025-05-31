integer = int(input("Enter the size of the pattern: "))
if integer <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    while row < integer:
        for col in range(integer):
            print("*", end="")
        print()
        row += 1