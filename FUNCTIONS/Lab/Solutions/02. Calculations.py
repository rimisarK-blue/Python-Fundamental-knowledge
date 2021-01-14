def calculation(action, num1, num2):
    if action == 'multiply':
        return num1 * num2
    elif action == 'divide':
        return num1 // num2
    elif action == 'add':
        return num1 + num2
    elif action == 'subtract':
        return num1 - num2


action_s = input()
number_1 = int(input())
number_2 = int(input())
print(calculation(action_s, number_1, number_2))


