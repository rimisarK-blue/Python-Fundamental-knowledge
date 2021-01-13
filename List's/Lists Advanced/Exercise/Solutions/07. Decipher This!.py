
sentence = input().split()

def extract_digit(text):
    return "".join(list(filter(str.isdigit, text)))


word = ''
for el in range(len(sentence)):
    word += (chr(int(extract_digit(sentence[el]))))

    for char in sentence[el]:
        if char.isalpha():
            word += char
    word_as_list = list(word)
    word_as_list[1], word_as_list[-1] = word_as_list[-1], word_as_list[1]
    word = ''.join(word_as_list)

    print(word, end=' ')
    word = ''
