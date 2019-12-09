def get_mode1(output, i):
    mode = str(output[i])[:len(str(output[i])) - 2]
    if (len(mode) == 0):
        return (0)
    else:
        return(int(mode[len(mode) - 1]))

def get_mode2(output, i):
    mode = str(output[i])[:len(str(output[i])) - 2]
    if (len(mode) == 0):
        return (0)
    elif (len(mode) > 1):
        return(int(mode[len(mode) - 2]))
    else:
        return (0)

def get_mode3(output, i):
    mode = str(output[i])[:len(str(output[i])) - 2]
    if (len(mode) == 0):
        return (0)
    elif (len(mode) > 2):
        return(int(mode[len(mode) - 3]))
    else:
        return (0)

def add_operation(output, i, relative_base):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    mode3 = get_mode3(output, i)
    pos1 = output[i + 1]
    pos2 = output[i + 2]
    if (mode3 == 0):
        pos_to_store = output[i + 3]
    elif (mode3 == 2):
        pos_to_store = relative_base + output[i + 3]

    if (mode1 == 0):
        add_value1 = output[pos1]
    elif (mode1 == 1):
        add_value1 = pos1
    elif (mode1 == 2):
        add_value1 = output[relative_base + pos1]
    if (mode2 == 0):
        add_value2 = output[pos2]
    elif (mode2 == 1):
        add_value2 = pos2
    elif (mode2 == 2):
        add_value2 = output[relative_base + pos2]

    value = add_value1 + add_value2
    if (pos_to_store < len(output)):
        output[pos_to_store] = value
    return (output)

def multiply_operation(output, i, relative_base):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    mode3 = get_mode3(output, i)

    pos1 = output[i + 1]
    pos2 = output[i + 2]
    if (mode3 == 0):
        pos_to_store = output[i + 3]
    elif (mode3 == 2):
        pos_to_store = relative_base + output[i + 3]


    if (mode1 == 0):
        mult_value1 = output[pos1]
    elif (mode1 == 1):
        mult_value1 = pos1
    elif (mode1 == 2):
        mult_value1 = output[relative_base + pos1]
    if (mode2 == 0):
        mult_value2 = output[pos2]
    elif (mode2 == 1):
        mult_value2 = pos2
    elif (mode2 == 2):
        mult_value2 = output[relative_base + pos2]

    value = mult_value1 * mult_value2
    if (pos_to_store < len(output)):
        output[pos_to_store] = value
    return (output)

def store_operation(output, i, relative_base):
    mode1 = get_mode1(output, i)
    value = int(input())
    if (mode1 == 0):
        pos = output[i + 1]
    elif (mode1 == 2):
        pos = relative_base + output[i + 1]

    output[pos] = value
    return (output)

def print_operation(output, i, relative_base):
    mode1 = get_mode1(output, i)
    if (mode1 == 0):
        print(output[output[i + 1]])
    elif (mode1 == 1):
        print(output[i + 1])
    elif (mode1 == 2):
        print(output[relative_base + output[i + 1]])

def jump_if_true_operation(output, i, relative_base):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    mode3 = get_mode3(output, i)

    if (mode1 == 0):
        arg1 = output[output[i + 1]]
    elif (mode1 == 1):
        arg1 = output[i + 1]
    elif (mode1 == 2):
        arg1 = output[relative_base + output[i + 1]]
    if (mode2 == 0):
        arg2 = output[output[i + 2]]
    elif (mode2 == 1):
        arg2 = output[i + 2]
    elif (mode2 == 2):
        arg2 = output[relative_base + output[i + 2]]

    if (arg1 != 0):
        if (mode3 == 0):
            return (arg2)
        elif (mode3 == 2):
            return (relative_base + arg2)
    else:
        return (i + 3)

def jump_if_false_operation(output, i, relative_base):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    mode3 = get_mode3(output, i)

    if (mode1 == 0):
        arg1 = output[output[i + 1]]
    elif (mode1 == 1):
        arg1 = output[i + 1]
    elif (mode1 == 2):
        arg1 = output[relative_base + output[i + 1]]
    if (mode2 == 0):
        arg2 = output[output[i + 2]]
    elif (mode2 == 1):
        arg2 = output[i + 2]
    elif (mode2 == 2):
        arg2 = output[relative_base + output[i + 1]]

    if (arg1 == 0):
        if (mode3 == 0):
            return (arg2)
        elif (mode3 == 2):
            return (relative_base + arg2)
    else:
        return (i + 3)

def if_less_than_operation(output, i, relative_base):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    mode3 = get_mode3(output, i)

    if (mode1 == 0):
        arg1 = output[output[i + 1]]
    elif (mode1 == 1):
        arg1 = output[i + 1]
    elif (mode1 == 2):
        arg1 = output[relative_base + output[i + 1]]
    if (mode2 == 0):
        arg2 = output[output[i + 2]]
    elif (mode2 == 1):
        arg2 = output[i + 2]
    elif (mode2 == 2):
        arg2 = output[relative_base + output[i + 2]]

    if (mode3 == 0):
        pos_to_store = output[i + 3]
    elif (mode3 == 2):
        pos_to_store = relative_base + output[i + 3]

    if (arg1 < arg2):
        output[pos_to_store] = 1
    else:
        output[pos_to_store] = 0

def if_equal_operation(output, i, relative_base):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    mode3 = get_mode3(output, i)

    if (mode1 == 0):
        arg1 = output[output[i + 1]]
    elif (mode1 == 1):
        arg1 = output[i + 1]
    elif (mode1 == 2):
        arg1 = output[relative_base + output[i + 1]]
    if (mode2 == 0):
        arg2 = output[output[i + 2]]
    elif (mode2 == 1):
        arg2 = output[i + 2]
    elif (mode2 == 2):
        arg2 = output[relative_base + output[i + 2]]

    if (mode3 == 0):
        pos_to_store = output[i + 3]
    elif (mode3 == 2):
        pos_to_store = relative_base + output[i + 3]

    if (arg1 == arg2):
        output[pos_to_store] = 1
    else:
        output[pos_to_store] = 0

def change_relative_base(output, i, relative_base):
    mode1 = get_mode1(output, i)
    arg1 = output[i + 1]

    if (mode1 == 0):
        relative_base += output[arg1]
    elif (mode1 == 1):
        relative_base += arg1
    elif (mode1 == 2):
        relative_base += output[relative_base + arg1]
    return (relative_base)

def run_program_alarm(intcode):
    output = list(intcode)
    relative_base = 0
    i = 0

    while (i < len(output)):
        opcode = output[i]
        print("opcode: " + str(opcode))
        if (int(str(opcode)[len(str(opcode)) - 2:]) == 1):
            output = add_operation(output, i, relative_base)
            i += 4
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 2):
            output = multiply_operation(output, i, relative_base)
            i += 4
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 3):
            output = store_operation(output, i, relative_base)
            i += 2
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 4):
            print_operation(output, i, relative_base)
            i += 2
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 5):
            i = jump_if_true_operation(output, i, relative_base)
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 6):
            i = jump_if_false_operation(output, i, relative_base)
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 7):
            if_less_than_operation(output, i, relative_base)
            i += 4
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 8):
            if_equal_operation(output, i, relative_base)
            i += 4
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 9):
            relative_base = change_relative_base(output, i, relative_base)
            i += 2
        elif (opcode == 99):
            break
    return (output)

if __name__ == "__main__":
    f = open("input", "r")

    intcode_input = f.read()
    intcode_input = list(map(int, intcode_input.split(',')))

    for i in range(30000):
        intcode_input.append(0)
    # intcode_input = list(map(int, input().split(',')))

    output = run_program_alarm(intcode_input)