file = open('data.txt', 'r')
lines = file.readlines()
dataset = []
increasing = 0
for line in lines:
    dataset.append(int(line))
iteration = 0
while iteration <= len(dataset) - 3:
    if iteration == 0:
        old = dataset[iteration] + dataset[iteration + 1] + dataset[iteration + 2]
    else:
        new = dataset[iteration] + dataset[iteration + 1] + dataset[iteration + 2]
        if new > old:
            increasing += 1
        old = new
    iteration += 1
print(increasing)