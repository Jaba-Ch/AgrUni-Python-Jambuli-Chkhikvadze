print("Divisor Finder")
n = int(input("Enter number: "))

if n < 1 or n > 1000:
    print("Number must be a natural number not greater than 1000.")
else:
    for j in range(1, n + 1):
        if n % j == 0:
            print(j, end=" ")