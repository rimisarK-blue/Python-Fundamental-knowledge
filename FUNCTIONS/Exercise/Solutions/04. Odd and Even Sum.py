def odd_even_calculator(num):
    result = 0
    result_2 = 0
    res = list(map(int, str(num)))

    for index in range(0, len(res)):
        res[index] = int(res[index])
        if not res[index] % 2 == 0:
            result += res[index]
        else:
            result_2 += res[index]
    return f'Odd sum = {str(result)}, Even sum = {str(result_2)}'


number = int(input())
print(odd_even_calculator(number))