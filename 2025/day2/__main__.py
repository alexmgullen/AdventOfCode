"""
As you can see from the `is_repeating` function, I also decided to try out some python type annotations and pydoc comments today.
"""

def part2(ranges):
    total = 0
    for r in ranges.split(","):
        lowest, highest = r.split('-')
        for i in range(int(lowest), int(highest) + 1):
            if is_repeating(str(i)):
                total += i

    return total

def is_repeating(s: str) -> bool:
    """
    this function splits each string until the halfway point to determin if the string is made up of reapeating numbers.
    """

    for i in range(1,(len(s) // 2) + 1):
        current = s[:i]

        #this effectively divides string 's' into equal parts of size 'i'
        matches = [s[j:j+i] for j in range(0, len(s), i)]

        matching = True
        for m in matches[1:]:
            if current != m:
                matching = False

        if matching:
            return True

    return False

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

    test_file = open('test1.txt','r')
    test_data = test_file.read()
    test_file.close()

    print(f'part 2 - test 1 output : {part2(test_data)}')

    input_file = open('input1.txt','r')
    input_data = input_file.read()
    input_file.close()

    print(f'part 2 - output : {part2(input_data)}')
