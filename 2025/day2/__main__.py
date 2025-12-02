
def part1(ranges):
    total = 0
    for r in ranges.split(","):
        lowest, highest = r.split('-')

        for i in range(int(lowest), int(highest) + 1):
            s = str(i)
            start, end = s[:len(s) // 2], s[len(s) // 2:]
            if start == end:
                total += i

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
