

inputs = []
for i in range(100):
    inputs.append(int(input()))

fuels = []
fuel_needed = 0
for i in range(len(inputs)):
    fuel_needed = int(inputs[i] / 3) - 2
    fuels.append(fuel_needed)
    fuel_needed = int(fuel_needed / 3) - 2
    while (fuel_needed > 0):
        fuels[i] += fuel_needed
        fuel_needed = int(fuel_needed / 3) - 2

print(sum(fuels))