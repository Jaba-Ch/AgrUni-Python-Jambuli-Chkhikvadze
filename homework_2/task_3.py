print("Leap Year Checker")
while True:
    raw = input("Enter year: ").strip()

    if raw.isdigit() and int(raw) > 0:
        year = int(raw)
        break

    print("Invalid input. Please enter a natural number.")
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")