#!/bin/python3

def is_sub_array(A, B, n, m):
    i = 0
    j = 0

    while (i < n and j < m):
        if (A[i] == B[j]):
            i += 1
            j += 1
            if (j == m):
                return (True)
        else:
            i += 1
            j = 0
    return (False)

def meets_requirements(combination):
    double = 0
    i = 0

    while (i < 6):
        if i > 0 and combination[i] < combination[i - 1]:
            return (0)
        i += 1

    for j in range(10):
        if (combination.count(str(j)) == 2) and (str(j) + str(j)) in combination:
            double = 1
    return (double)

print(meets_requirements(str(112233)))
print(meets_requirements(str(123444)))
print(meets_requirements(str(111122)))
print(meets_requirements(str(112223)))
print(meets_requirements(str(133322)))


def get_passwords():
    passwords = []

    for nb in range(125730, 579381):
        if (meets_requirements(str(nb))):
            passwords.append(nb)
    return (passwords)

if __name__ == '__main__':
    passwords = get_passwords()
    print(len(passwords))