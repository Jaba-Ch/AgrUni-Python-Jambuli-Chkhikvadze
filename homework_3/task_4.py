import random

original = [random.randint(1, 4) for _ in range(5)]

expanded = []
for num in original:
    expanded.extend([num] * num)

print("List -", expanded)
print("Length -", len(expanded))