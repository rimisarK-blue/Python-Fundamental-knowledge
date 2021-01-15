def smallest_num(num1, num2, num3):
    result = 0
    if num1 > 0:
        result = num1
    if num2 < num1:
        result = num2
    if num1 > num3 < num2:
        result = num3
    return result


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(smallest_num(number_1, number_2, number_3))