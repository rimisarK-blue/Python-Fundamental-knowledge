
palindromes = input().split()
chosen = input()

filter_palindromes = [word for word in palindromes if word == word[::-1]]

how_many = filter_palindromes.count(chosen)

print(filter_palindromes)
print(f'Found palindrome {how_many} times')