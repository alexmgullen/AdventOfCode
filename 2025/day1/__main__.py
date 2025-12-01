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

if __name__ == '__main__':
    test_file = open('test1.txt','r')
    test_data = test_file.read()
    test_file.close()

    print(f'test 1 input: {test_data}')
    print(f'test 1 output : {part1(test_data)}')

    input_file = open('input1.txt','r')
    input_data = input_file.read()
    input_file.close()

    print(f'input: {input_data}')
    print(f'output : {part1(input_data)}')
