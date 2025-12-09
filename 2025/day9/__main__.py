"""
Advent of Code Day9
"""

import math

def get_area(a,b) -> int:
    width = 0
    height = 0

    if b[0] <= a[0]:
        width = a[0] - b[0] + 1
    else:
        width = b[0] - a[0] + 1
    
    if b[1] <= a[1]:
        height = a[1] - b[1] + 1
    else:
        height = b[1] - a[1] + 1

    return width * height

def part1(floor: str) -> int:
    """
    """
    total = 1

    coords = []

    distances = {}

    for row in floor.strip().split('\n'):
        x = int(row.split(',')[0])
        y = int(row.split(',')[1])

        coords.append((x,y))

        for coord in coords[:-1]:
            distances[(coords[-1],coord)] = get_area(coords[-1],coord)

    for distance in distances:
        total = max(total,distances[distance])




    return total

if __name__ == '__main__':
    test_file = open('test1.txt','r')
    test_data = test_file.read()
    test_file.close()

    print(f'part 1 - test 1 output : {part1(test_data)}')

    input_file = open('input1.txt','r')
    input_data = input_file.read()
    input_file.close()

    print(f'part 1 - output : {part1(input_data)}')
