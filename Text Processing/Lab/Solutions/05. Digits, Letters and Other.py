
letter = ""
digits = ""
others = ""

text = input()
for char in text:
    if char.isalpha():
        letter += char
    elif char.isdigit():
        digits += char
    else:
        others += char

print(digits)
print(letter)
print(others)