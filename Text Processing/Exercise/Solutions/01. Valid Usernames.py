
usernames = input().split(', ')

valid_passwords = []

for user in usernames:
    count = 0
    if 3 <= len(user) <= 16:
        for char in user:
            if char.isdigit() or char.isalpha() or char == '-' or char == '_':
                count += 1
            if len(user) == count:
                valid_passwords.append(user)

for users in valid_passwords:
    print(users)


