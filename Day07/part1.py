import itertools

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

def store_operation(output, i, value):
    pos = output[i + 1]

    output[pos] = value
    return (output)

def print_operation(output, i):
    mode1 = get_mode1(output, i)
    if (mode1) == 0:
        return (str(output[output[i + 1]]))
    else:
        return (str(output[i + 1]))

def run_program_alarm(intcode, phase_setting, input_value):
    output = list(intcode)
    output_signal = ""
    input_mode = 1
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
            if input_mode == 1:
                output = store_operation(output, i, phase_setting)
                input_mode += 1
            else:
                output = store_operation(output, i, input_value)
            i += 2
        elif (int(str(opcode)[len(str(opcode)) - 2:]) == 4):
            output_signal += print_operation(output, i)
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
        # else:
        #     i += 1
    return (output_signal)

def allLexicographicRecur(string, data, last, index):
    length = len(string)

    # One by one fix all characters at the given index and
    # recur for the subsequent indexes
    for i in range(length):

        # Fix the ith character at index and if this is not
        # the last index then recursively call for higher
        # indexes
        data[index] = string[i]

        # If this is the last index then print the string
        # stored in data[]
        if index == last:
            all_phase_settings.append(data)
        else:
            allLexicographicRecur(string, data, last, index + 1)

        # This function sorts input string, allocate memory for data


# (needed for allLexicographicRecur()) and calls
# allLexicographicRecur() for printing all permutations
def allLexicographic(string):
    length = len(string)

    # Create a temp array that will be used by
    # allLexicographicRecur()
    data = [""] * (length + 1)

    # Sort the input string so that we get all output strings in
    # lexicographically sorted order
    string = sorted(string)

    # Now print all permutaions
    allLexicographicRecur(string, data, length - 1, 0)

if __name__ == "__main__":
    f = open("input", "r")

    intcode_input = f.read()
    intcode_input = list(map(int, intcode_input.split(',')))

    # intcode_input = list(map(int, input().split(',')))
    # allLexicographic('01234')
    all_phase_settings = itertools.permutations(['0', '1', '2', '3', '4'], 5)
    greatest = 0
    # print(list(all_phase_settings))
    for phase_setting in all_phase_settings:
        input_signal = 0
        for i in range(5):
            output_signal = run_program_alarm(intcode_input, int(phase_setting[i]), input_signal)
            input_signal = int(output_signal)
        if (int(output_signal) > greatest):
            greatest = int(output_signal)

    print(greatest)