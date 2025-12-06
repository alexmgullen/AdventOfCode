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
    """
    Transform the homework into a 3d list, then find every vertical line full of blank lines in the list and add them to an array, seperate the array into columns using those breaks then iterate negatively over those columns in reverse to produce a list of the numbers vertically from right to left. finally take those numbers and perform each operation on the list of numbers, add them to a list, and sum them all together to get a grand total.
    """

    # convert the homework into a 3d array
    sheet = [list(x) for x in homework.strip().split('\n')[:-1]]

    # find every column where a space goes from the bottom of the worksheet
    # to the top
    breaks = [-1]

    # iterate over each x and if x is a space, check the rest of y and see if those are
    # spaces too
    for x in range(len(sheet[0])):
        if sheet[0][x] == ' ':
            is_break = True
            for y in range(len(sheet)):
                if sheet[y][x] != ' ':
                    is_break = False
                    break

            if is_break:
                breaks.append(x)
    breaks.append(len(sheet[0]))

    # seperate the input into columns
    columns = []
    for b in range(1,len(breaks)):
        column = []
        for row in range(len(sheet)):
            column.append(sheet[row][(breaks[b-1] + 1):breaks[b]])
        columns.append(column)
    
    numbers = []

    # convert the columns to numbers using cephelapod math
    for column in columns:
        number_stack = []
        for y in range(len(column[0]) -1, -1,-1):
            n_stack = []
            for x in range(len(column)):
                if column[x][y] != ' ':
                    n_stack.append(column[x][y])
            number_stack.append(int(''.join(n_stack)))

        numbers.append(number_stack)

    # extract each operation from the homework
    operations = list(homework.strip().split('\n')[-1].replace(' ',''))

    # perform each operation on the columns of numbers given
    sums = []

    for i in range(len(operations)):
        operation = operations[i]
        s = 0
        if operation == '*':
            s += 1

        for y in range(len(numbers[i])):
            if operation == '*':
                s *= numbers[i][y]
            elif operation == '+':
                s += numbers[i][y]
        sums.append(s)

    # return the grand total of all numbers
    return sum(sums)





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
