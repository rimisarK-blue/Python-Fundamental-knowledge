
str1, str2 = input().split()

total_sum = 0

if len(str1) == len(str2):
    for i in range(len(str1)):
        total_sum += ord(str1[i]) * ord(str2[i])

elif len(str1) > len(str2):
    for i in range(len(str2)):
        total_sum += ord(str2[i]) * ord(str1[i])
    for i in range(len(str2), len(str1)):
        total_sum += ord(str1[i])

elif len(str1) < len(str2):
    for i in range(len(str1)):
        total_sum += ord(str1[i]) * ord(str2[i])
    for i in range(len(str1), len(str2)):
        total_sum += ord(str2[i])

print(total_sum)