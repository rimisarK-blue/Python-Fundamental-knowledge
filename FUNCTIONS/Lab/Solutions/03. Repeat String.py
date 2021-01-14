
def repeat_string(string, rep):
    result = ''
    for i in range(0, rep):
        result += string
    return result


name = input()
number = int(input())
print(repeat_string(name, number))
