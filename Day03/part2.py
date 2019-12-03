def go_right(start_point, command, points, steps):
    for i in range(int(command[1:])):
        start_point[0] += 1
        steps += 1
        points.append([start_point[0], start_point[1], steps])
    return (steps)

def go_left(start_point, command, points, steps):
    for i in range(int(command[1:])):
        start_point[0] -= 1
        steps += 1
        points.append([start_point[0], start_point[1], steps])
    return (steps)

def go_up(start_point, command, points, steps):
    for i in range(int(command[1:])):
        start_point[1] += 1
        steps += 1
        points.append([start_point[0], start_point[1], steps])
    return (steps)

def go_down(start_point, command, points, steps):
    for i in range(int(command[1:])):
        start_point[1] -= 1
        steps += 1
        points.append([start_point[0], start_point[1], steps])
    return (steps)

def draw_line(start_point, command, points, steps):
    if (command[0] == 'R'):
        steps = go_right(start_point, command, points, steps)
    elif (command[0] == 'L'):
        steps = go_left(start_point, command, points, steps)
    elif (command[0] == 'U'):
        steps = go_up(start_point, command, points, steps)
    elif (command[0] == 'D'):
        steps = go_down(start_point, command, points, steps)
    return (steps)


def draw_lines(input):
    steps = 0
    points = []
    point = [0, 0]
    for command in input:
        steps = draw_line(point, command, points, steps)
    return (points)

def get_steps(points1, points2):
    steps = 99999999999

    for point1 in points1:
        for point2 in points2:
            if point1[:2] == point2[:2]:
                if (point1[2] + point2[2] < steps):
                    steps = point1[2] + point2[2]
    return (steps)

def get_intersection_distance(input1, input2):
    points1 = draw_lines(input1)
    points2 = draw_lines(input2)
    distance = get_steps(points1, points2)
    print(distance)

if __name__ == "__main__":
    input1 = list(input().split(','))
    input2 = list(input().split(','))

    get_intersection_distance(input1, input2)