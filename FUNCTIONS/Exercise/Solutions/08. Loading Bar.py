
def loader(bars_list, num_bars_to_replace):
    for index in range(num_bars_to_replace):
        bars_list[index] = '%'
    return bars_list


bars = []
for i in range(10):
    bars.append('.')

percent = int(input())
bars_to_fill = percent // 10

loader_result = (loader(bars, bars_to_fill))

if percent < 100:
    print(f'{percent}% [{"".join(loader_result)}]')
    print('Still loading...')
else:
    print('100% Complete!')
    print('[%%%%%%%%%%]')