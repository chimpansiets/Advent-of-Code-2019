#!/bin/python3
import array as arr

def meets_requirements(combination):
    double = 0
    i = 0

    while (i < 6):
        if i > 0 and combination[i] == combination[i - 1]:
            double = 1
        if i > 0 and combination[i] < combination[i - 1]:
            return (0)
        i += 1
    return (double)

def get_passwords():
    passwords = []

    for nb in range(125730, 579381):
        if (meets_requirements(str(nb))):
            passwords.append(nb)
    return (passwords)

if __name__ == '__main__':
    passwords = get_passwords()
    print(len(passwords))