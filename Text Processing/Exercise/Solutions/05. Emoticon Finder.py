
data = input()
index = 0
emotion = []
while index < len(data):
    if data[index] == ':':
        emotion.append(data[index])
        emotion.append(data[index+1])
        print(''.join(emotion))
        emotion = []
        index +=1
    else:
        index += 1
        continue
