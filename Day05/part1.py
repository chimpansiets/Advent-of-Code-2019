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
        return(1)
    else:
        return (0)

def add_operation(output, i):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    pos1 = output[i + 1]
    pos2 = output[i + 2]
    pos_to_store = output[i + 3]

    if (mode1 == 0):
        add_value1 = output[pos1]
    else:
        add_value1 = pos1
    if (mode2 == 0):
        add_value2 = output[pos2]
    else:
        add_value2 = pos2

    value = add_value1 + add_value2
    if (pos_to_store < len(output)):
        output[pos_to_store] = value
    return (output)

def multiply_operation(output, i):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    pos1 = output[i + 1]
    pos2 = output[i + 2]
    pos_to_store = output[i + 3]

    if (mode1 == 0):
        mult_value1 = output[pos1]
    else:
        mult_value1 = pos1
    if (mode2 == 0):
        mult_value2 = output[pos2]
    else:
        mult_value2 = pos2

    value = mult_value1 * mult_value2
    if (pos_to_store < len(output)):
        output[pos_to_store] = value
    return (output)

def store_operation(output, i):
    value = int(input())
    pos = output[i + 1]

    output[pos] = value
    return (output)

def print_operation(output, i):
    mode1 = get_mode1(output, i)
    if (mode1) == 0:
        print(output[output[i + 1]])
    else:
        print(output[i + 1])

def jump_if_true_operation(output, i):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    if (mode1 == 0):
        arg1 = output[output[i + 1]]
    else:
        arg1 = output[i + 1]
    if (mode2 == 0):
        arg2 = output[output[i + 2]]
    else:
        arg2 = output[i + 2]

    if (arg1 != 0):
        return (arg2)
    else:
        return (i + 3)

def jump_if_false_operation(output, i):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    if (mode1 == 0):
        arg1 = output[output[i + 1]]
    else:
        arg1 = output[i + 1]
    if (mode2 == 0):
        arg2 = output[output[i + 2]]
    else:
        arg2 = output[i + 2]

    if (arg1 == 0):
        return (arg2)
    else:
        return (i + 3)

def if_less_than_operation(output, i):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    if (mode1 == 0):
        arg1 = output[output[i + 1]]
    else:
        arg1 = output[i + 1]
    if (mode2 == 0):
        arg2 = output[output[i + 2]]
    else:
        arg2 = output[i + 2]
    pos_to_store = output[i + 3]

    if (arg1 < arg2):
        output[pos_to_store] = 1
    else:
        output[pos_to_store] = 0

def if_equal_operation(output, i):
    mode1 = get_mode1(output, i)
    mode2 = get_mode2(output, i)
    if (mode1 == 0):
        arg1 = output[output[i + 1]]
    else:
        arg1 = output[i + 1]
    if (mode2 == 0):
        arg2 = output[output[i + 2]]
    else:
        arg2 = output[i + 2]
    pos_to_store = output[i + 3]

    if (arg1 == arg2):
        output[pos_to_store] = 1
    else:
        output[pos_to_store] = 0

def run_program_alarm(intcode):
    output = list(intcode)
    i = 0

    while (i < len(output)):
        opcode = output[i]
        if (int(str(opcode)[len(str(opcode)) - 2:]) == 1):
            output = add_operation(output, i)
            i += 4
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 2):
            output = multiply_operation(output, i)
            i += 4
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 3):
            output = store_operation(output, i)
            i += 2
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 4):
            print_operation(output, i)
            i += 2
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 5):
            i = jump_if_true_operation(output, i)
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 6):
            i = jump_if_false_operation(output, i)
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 7):
            if_less_than_operation(output, i)
            i += 4
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 8):
            if_equal_operation(output, i)
            i += 4
        elif (opcode == 99):
            break
    return (output)

if __name__ == "__main__":
    f = open("input", "r")

    intcode_input = f.read()
    intcode_input = list(map(int, intcode_input.split(',')))

    # intcode_input = list(map(int, input().split(',')))

    output = run_program_alarm(intcode_input)