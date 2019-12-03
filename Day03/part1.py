def go_right(start_point, command, points):
    for i in range(int(command[1:])):
        start_point[0] += 1
        points.append([start_point[0], start_point[1]])

def go_left(start_point, command, points):
    for i in range(int(command[1:])):
        start_point[0] -= 1
        points.append([start_point[0], start_point[1]])

def go_up(start_point, command, points):
    for i in range(int(command[1:])):
        start_point[1] += 1
        points.append([start_point[0], start_point[1]])

def go_down(start_point, command, points):
    for i in range(int(command[1:])):
        start_point[1] -= 1
        points.append([start_point[0], start_point[1]])

def draw_line(start_point, command, points):
    if (command[0] == 'R'):
        go_right(start_point, command, points)
    elif (command[0] == 'L'):
        go_left(start_point, command, points)
    elif (command[0] == 'U'):
        go_up(start_point, command, points)
    elif (command[0] == 'D'):
        go_down(start_point, command, points)


def draw_lines(input):
    points = []
    point = [0, 0]
    for command in input:
        draw_line(point, command, points)
    return (points)

def get_least_distance(points1, points2):
    least_distance = 999999999

    for point in points1:
        if (abs(point[0]) + abs(point[1]) < least_distance):
            if point in points2:
                least_distance = abs(point[0]) + abs(point[1])

    return (least_distance)

def get_intersection_distance(input1, input2):
    points1 = draw_lines(input1)
    points2 = draw_lines(input2)
    distance = get_least_distance(points1, points2)
    print(distance)

if __name__ == "__main__":
    input1 = list(input().split(','))
    input2 = list(input().split(','))

    get_intersection_distance(input1, input2)