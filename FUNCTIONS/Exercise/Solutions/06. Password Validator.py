
def pass_check(password):
    valid_password = True

    if not (6 <= len(password) <= 10):
        valid_password = False
        print("Password must be between 6 and 10 characters")

    for el in password:
        if not el.isdigit() and not el.isalpha():
            valid_password = False
            print("Password must consist only of letters and digits")
            break

    count_digits = 0
    for el in password:
        if el.isdigit():
            count_digits += 1

    if count_digits < 2:
        valid_password = False
        print("Password must have at least 2 digits")

    return valid_password


password = input()
pass_good = pass_check(password)

if pass_good is True:
    print("Password is valid")

