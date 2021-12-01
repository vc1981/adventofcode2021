file = open('data.txt', 'r')
lines = file.readlines()
old =  0
iteration = 0
increas_count = 0
decrease_count  = 0
for line in lines:
    new = int(line)
    if new > old and iteration != 0:
        increas_count +=  1
        print('New: ' + str(new) + ' Old: ' + str(old) + ' Increasing ' + str(increas_count))
    elif old > new and iteration != 0:
        decrease_count += 1
        print('New: ' + str(new) + ' Old: ' + str(old) + ' Decreasing ' + str(decrease_count))
    else:
        print('Heck')
    old = new
    iteration =+ 1
