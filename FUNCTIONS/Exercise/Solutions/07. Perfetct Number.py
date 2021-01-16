
def perfect_number(n):

    good_numbers = []
    for nums in range(1, n):
        if n % nums == 0:
            good_numbers.append(nums)

    if sum(good_numbers) == n:
        return True
    return False


number = int(input())
if perfect_number(number):
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')
