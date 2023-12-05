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
        while len(cubes) > 0:
            cube = cubes.pop()
            cube = cube.strip()
            cube = cube.split(' ')

            value = int(cube[0])
            color = cube[1]
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
total_power = 0

# Part 2
for line in lines:
    line = line.rstrip()
    is_valid = True
    game = line.split(':')[0]
    game_id = game.split(' ')[1]
    data = line.split(':')[1]
    hands = data.split(';')
    red_cubes = []
    green_cubes = []
    blue_cubes = []

    for hand in hands:
        hand = hand.strip()
        cubes = hand.split(',')
        
        while len(cubes) > 0:
            cube = cubes.pop()
            cube = cube.strip()
            cube = cube.split(' ')

            value = int(cube[0])
            color = cube[1]
            
            if color == 'red':
                red_cubes.append(value)
            elif color == 'green':
                green_cubes.append(value)
            elif color == 'blue':
                blue_cubes.append(value)

    max_red = max(red_cubes)
    max_green = max(green_cubes)
    max_blue = max(blue_cubes)
    total_power += max_red * max_green * max_blue

    if is_valid:
        valid_game_id_total += int(game_id)


print("Part 2 solution:", total_power)