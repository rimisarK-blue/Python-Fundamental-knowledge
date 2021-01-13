
rooms = int(input())

free_chairs = 0
enough_chairs = False

for room in range(1, rooms+1):
    chair, taken_places = input().split()
    taken_places = int(taken_places)
    needed_chair = 0

    if len(chair) < taken_places:
        needed_chair += taken_places - len(chair)
        enough_chairs = True
        print(f'{needed_chair} more chairs needed in room {room}')
    elif len(chair) > taken_places:
        free_chairs += len(chair) - taken_places


if not enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")




