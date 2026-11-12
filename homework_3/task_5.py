s1 = input().strip()
s2 = input().strip()

if sorted(s1.lower()) == sorted(s2.lower()):
    print("YES")
else:
    print("NO")