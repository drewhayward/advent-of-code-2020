import math

def get_instructions():
    navs = []
    with open('day12/input') as f:
        for line in f.readlines():
            nav = line.strip()
            navs.append([nav[0], int(nav[1:])])
    return navs

def apply_instruction(nav, position):
    new_pos = position[:]
    num = nav[1]
    if nav[0] == 'N':
        new_pos[1] += num
    elif nav[0] == 'S':
        new_pos[1] -= num
    elif nav[0] == 'E':
        new_pos[0] += num
    elif nav[0] == 'W':
        new_pos[0] -= num
    elif nav[0] == 'L':
        new_pos[2] = (new_pos[2] + math.radians(num)) % (math.pi * 2)
    elif nav[0] == 'R':
        new_pos[2] = (new_pos[2] - math.radians(num)) % (math.pi * 2)
    elif nav[0] == 'F':
        rads = new_pos[2]
        new_pos[0] += math.cos(rads) * num
        new_pos[1] += math.sin(rads) * num
    
    return new_pos

def apply_instruction_way(nav, waypoint, position):
    new_pos = position[:]
    new_way = waypoint[:]
    num = nav[1]
    if nav[0] == 'N':
        new_way[1] += num
    elif nav[0] == 'S':
        new_way[1] -= num
    elif nav[0] == 'E':
        new_way[0] += num
    elif nav[0] == 'W':
        new_way[0] -= num
    elif nav[0] == 'L':
        try:
            angle = math.atan(waypoint[1]/waypoint[0])
            if waypoint[0] > 0 and waypoint[1] < 0:
                angle += math.pi*2
            elif not (waypoint[0] >= 0 and waypoint[1] >= 0):
                angle += math.pi
        except ZeroDivisionError:
            if waypoint[1] > 0:
                angle = math.pi / 2
            else:
                angle = 3 * math.pi / 2
        
        angle = (angle + math.radians(num)) % (math.pi*2)
        dist = math.sqrt(waypoint[0]**2 + waypoint[1]**2)
        new_way[0] = round(dist * math.cos(angle))
        new_way[1] = round(dist * math.sin(angle))
    elif nav[0] == 'R':
        try:
            angle = math.atan(waypoint[1]/waypoint[0])
            if waypoint[0] > 0 and waypoint[1] < 0:
                angle += math.pi*2
            elif not (waypoint[0] >= 0 and waypoint[1] >= 0):
                angle += math.pi
        except ZeroDivisionError:
            if waypoint[1] > 0:
                angle = math.pi / 2
            else:
                angle = 3 * math.pi / 2
        angle = (angle - math.radians(num)) % (math.pi*2)
        dist = math.sqrt(waypoint[0]**2 + waypoint[1]**2)
        new_way[0] = (dist * math.cos(angle))
        new_way[1] = (dist * math.sin(angle))
    elif nav[0] == 'F':
        new_pos[0] += waypoint[0] * num
        new_pos[1] += waypoint[1] * num
    
    return new_way, new_pos

def part_1():
    position = [0, 0, 0] # x, y, heading
    for nav in get_instructions():
        position = apply_instruction(nav, position)

    return abs(position[0]) + abs(position[1])

def part_2():
    waypoint = [10, 1]
    position = [0, 0]
    for nav in get_instructions():
        waypoint, position = apply_instruction_way(nav, waypoint, position)

    return abs(position[0]) + abs(position[1])

def testing():
    waypoint = [0, 0]
    position = [0, 0]
    while True:
        print(f"Position: {position}")
        print(f"Waypoint: {waypoint}")
        nav = input('Nav: ')
        nav = [nav[0], int(nav[1:])]

        waypoint, position = apply_instruction_way(nav, waypoint, position)



if __name__ == "__main__":
    #testing()
    print(part_1())
    print(part_2())