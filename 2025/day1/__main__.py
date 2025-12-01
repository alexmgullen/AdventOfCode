import math

def part1(combination):
    total = 0
    current = 50

    for line in combination.split('\n'):
        if len(line) > 1:

            ticks =  int(line[1:])

            if line[0] == 'L':
                current -= ticks
            elif line[0] == 'R':
                current += ticks

            current %= 100

            if current == 0:
                total += 1

    return total

def part2(combination):
    total = 0
    current = 50

    for line in combination.split('\n'):
        if len(line) > 1:

            ticks =  int(line[1:])

            if line[0] == 'L':
                for i in range(ticks):
                    current -= 1
                    current %= 100
                    if current == 0:
                        total += 1
            elif line[0] == 'R':
                for i in range(ticks):
                    current += 1
                    current %= 100
                    if current == 0:
                        total += 1
    return total

if __name__ == '__main__':
    test_file = open('test1.txt','r')
    test_data = test_file.read()
    test_file.close()

    print(f'part 1 - test 1 input: {test_data}')
    print(f'part 1 - test 1 output : {part1(test_data)}')

    input_file = open('input1.txt','r')
    input_data = input_file.read()
    input_file.close()

    print(f'part 1 - input: {input_data}')
    print(f'part 1 - output : {part1(input_data)}')

    ### Part 2 ###

    print(f'part 2 - test 1 input: {test_data}')
    print(f'part 2 - test 1 output : {part2(test_data)}')

    test_file = open('test2.txt','r')
    test_data = test_file.read()
    test_file.close()

    print(f'part 2 - test 2 input: {test_data}')
    print(f'part 2 - test 2 output : {part2(test_data)}')

    print(f'part 2 - input: {input_data}')
    print(f'part 2 - output : {part2(input_data)}')
