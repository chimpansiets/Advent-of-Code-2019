
def add_operation(output, i):
    pos1 = output[i + 1]
    pos2 = output[i + 2]
    pos_to_store = output[i + 3]

    value = output[pos1] + output[pos2]
    if (pos_to_store < len(output)):
        output[pos_to_store] = value
    return (output)

def multiply_operation(output, i):
    pos1 = output[i + 1]
    pos2 = output[i + 2]
    pos_to_store = output[i + 3]

    value = output[pos1] * output[pos2]
    if (pos_to_store < len(output)):
        output[pos_to_store] = value
    return (output)

def run_program_alarm(input):
    output = list(input)
    i = 0

    while (i < len(output)):
        opcode = output[i]
        if (opcode == 1):
            output = add_operation(output, i)
        elif (opcode == 2):
            output = multiply_operation(output, i)
        elif (opcode == 99):
            break
        i += 4
    return (output)

if __name__ == "__main__":
    input = list(map(int, input().split(',')))

    for noun in range(100):
        for verb in range(100):
            input[1] = noun
            input[2] = verb
            output = run_program_alarm(input)
            if (output[0] == 19690720):
                print(output)
