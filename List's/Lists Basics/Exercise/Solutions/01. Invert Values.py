numbers_prime = input().split()


for i in range(0, len(numbers_prime)):
    numbers_prime[i] = int(numbers_prime[i])
for i in range(0, len(numbers_prime)):
    if numbers_prime[i] >= 0:
        numbers_prime[i] = numbers_prime[i] * -1

        continue
    if numbers_prime[i] < 0:
        numbers_prime[i] = abs(numbers_prime[i])
        continue

print(numbers_prime)


