
class Layer:
    def __init__(self, layer_id):
        self.values = []
        self.layer_id = layer_id

    def add_row(self, row):
        self.values.append(row)

def part1(layers):
    least_zeroes = 9999999999
    layer_id = 0
    for layer in layers:
        amount_zeroes = 0
        for row in layer.values:
            amount_zeroes += row.count('0')
        if (amount_zeroes < least_zeroes):
            least_zeroes = amount_zeroes
            layer_id = layer.layer_id

    img_values = layers[layer_id].values

    amount_ones = 0
    amount_twos = 0

    for row in img_values:
        amount_ones += row.count('1')
        amount_twos += row.count('2')

    print("Part1: " + str(amount_ones * amount_twos))

def check_colour(layers, x, y):
    for layer in layers:
        if (layer.values[y][x] == '0'):
            return ('0')
        elif (layer.values[y][x] == '1'):
            return ('1')
    return ('2')

def part2(layers, width, length):
    message = []

    for y in range(length):
        row = []
        for x in range(width):
            row.append(check_colour(layers, x, y))
        message.append(row)

    print("Part2: ")
    for row in message:
        print(' '.join(row))

if __name__ == "__main__":
    image_data = input()
    layers = []
    row = []
    layer_index = 0
    row_counter = 0
    width = 25
    length = 6
    curr_layer = Layer(layer_index)

    for i in range(len(image_data)):
        if (i % width == 0) and i != 0:
            curr_layer.values.append(row)
            row = []
            row_counter += 1
        if (row_counter == length):
            layers.append(curr_layer)
            layer_index += 1
            curr_layer = Layer(layer_index)
            row_counter = 0
        row.append(image_data[i])
    curr_layer.values.append(row)
    layers.append(curr_layer)

    part1(layers)
    part2(layers, width, length)