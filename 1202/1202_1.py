file = open('data.txt', 'r')
lines = file.readlines()
x_position = 0
y_position = 0
for line in lines:
    movement = str(line).split(' ')
    if movement[0] == 'forward':
        x_position += int(movement[1])
    elif movement[0] == 'up':
        y_position -= int(movement[1])
    elif movement[0] == 'down':
        y_position += int(movement[1])
print(x_position * y_position)

