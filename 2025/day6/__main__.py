import copy
"""
Advent of Code Day6
"""

def part1(homework: str) -> int:
    """
    Seperate the homework into the component number ordered by index, then extract the operations ordered by index, then perform the operation at the respective index for each number in the same index and return the sum of all those values.
    """
    sheet = []

    # convert the the numbers in the puzzle into a 3d array
    for row in homework.strip().split('\n')[:-1]:
        row_stack = []
        n_stack = []
        for char in row:
            if char != ' ':
                n_stack.append(char)
            elif char == ' ':
                if len(n_stack) > 0:
                    row_stack.append(int(''.join(n_stack)))
                n_stack = []
        
        # make sure to add any remaining values in the`n_stack` to the `row_stack` if we
        # don't have a whitespace at the end of our line
        if len(n_stack) > 0:
            row_stack.append(int(''.join(n_stack)))
        sheet.append(row_stack)

    # extract each operation from the homework
    operation_sheet = list(homework.strip().split('\n')[-1].replace(' ',''))

    sums = []
    # perform operation for each column
    for i in range(len(sheet[0])):
        operation = operation_sheet[i]
        s = 0
        
        # make sure that if we are doing multiplication we don't multiply by zero
        if operation == '*':
            s = 1

        for y in range(len(sheet)):
            if operation == '*':
                s *= sheet[y][i]
            elif operation == '+':
                s += sheet[y][i]

        sums.append(s)

    # Run the operation at index i for each vertical stack in the 3d array

    return sum(sums)

def part2(homework: str) -> int:


if __name__ == '__main__':
    test_file = open('test1.txt','r')
    test_data = test_file.read()
    test_file.close()

    print(f'part 1 - test 1 output : {part1(test_data)}')

    input_file = open('input1.txt','r')
    input_data = input_file.read()
    input_file.close()

    print(f'part 1 - output : {part1(input_data)}')
