# Part 1
file = open('input.txt', 'r')
lines = file.readlines()

max_red_cubes = 12
max_green_cubes = 13
max_blue_cubes = 14
valid_game_id_total = 0

for line in lines:
    line = line.rstrip()
    is_valid = True
    game = line.split(':')[0]
    game_id = game.split(' ')[1]
    data = line.split(':')[1]
    hands = data.split(';')
    

    for hand in hands:
        hand = hand.strip()
        cubes = hand.split(',')
        print ("HAND", hand)
        while len(cubes) > 0:
            cube = cubes.pop()
            cube = cube.strip()
            cube = cube.split(' ')

            value = int(cube[0])
            color = cube[1]
            print (color, value)
            if color == 'red' and int(value) > max_red_cubes:
                is_valid = False
            elif color == 'green' and int(value) > max_green_cubes:
                is_valid = False
            elif color == 'blue' and int(value) > max_blue_cubes:
                is_valid = False

            if not is_valid:
                break
            
    if is_valid:
        valid_game_id_total += int(game_id)

print("Part 1 solution:", valid_game_id_total)

