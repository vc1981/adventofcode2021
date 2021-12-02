file = open('data.txt', 'r')
lines = file.readlines()
iteration = 0
x_position = 0
y_position = 0
aim = 0
for line in lines:
    movement = str(line).split(' ')
    if movement[0] == 'forward':
        if aim == 0:
            x_position += int(movement[1])
        else:
            x_position += int(movement[1])
            y_position += aim * int(movement[1])
    elif movement[0] == 'up':
        aim -= int(movement[1])
    elif movement[0] == 'down':
        aim += int(movement[1])
print(x_position * y_position)

