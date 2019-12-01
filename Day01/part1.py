inputs = []
for i in range(100):
    inputs.append(int(input()))

fuels = []
for i in range(len(inputs)):
    fuel_needed = int(inputs[i] / 3) - 2
    fuels.append(fuel_needed)

print(sum(fuels))