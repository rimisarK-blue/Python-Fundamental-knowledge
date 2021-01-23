
data = input()

encrypted_code = ""
for char in data:
    encrypted = ord(char) + 3
    encrypted_code += chr(encrypted)

print(encrypted_code)


