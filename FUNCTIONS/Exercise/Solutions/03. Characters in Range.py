def in_the_middle(chr1, chr2):
    result = ''
    for i in range(ord(chr1)+1, ord(chr2)):
        result += (chr(i))
        result += ' '
    return result


char_1 = input()
char_2 = input()
print(in_the_middle(char_1, char_2))