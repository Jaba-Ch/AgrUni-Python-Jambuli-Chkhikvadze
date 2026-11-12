text = input("Enter text: ")

cleaned = ""
for c in text.lower():
    if 'a' <= c <= 'z':
        cleaned += c

if cleaned == cleaned[::-1]:
    print("Is palindrome")
else:
    print("Is not palindrome")