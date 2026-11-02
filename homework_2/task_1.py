print("Triangle Calculator")

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("These sides cannot form a triangle.")
else:
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")