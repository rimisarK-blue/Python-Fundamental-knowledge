
n_snow_balls = int(input())

max_snowball_snow = 0
max_snowball_time = 0
max_snowball_quality = 0

max_score = -1

for ball in range(1, n_snow_balls + 1):

    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    score = (snowball_snow / snowball_time) ** snowball_quality

    if score > max_score:
        max_score = score
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f"{max_snowball_snow} : {max_snowball_time} = {int(max_score)} ({max_snowball_quality})")