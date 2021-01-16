
def calc_factorial(n):
    result = 1
    for num in range(2, n+1):
        result *= num
    return result


number_1 = int(input())
number_2 = int(input())

fact_1_calculation = calc_factorial(number_1)
fact_2_calculation = calc_factorial(number_2)

result = fact_1_calculation / fact_2_calculation

print(f'{result:.2f}')
