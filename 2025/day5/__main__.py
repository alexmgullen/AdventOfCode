import copy
"""
Advent of Code Day5
"""

def part1(puzzle: str) -> int:
    """
    Seperate the puzzle input into ranges and ingredients, then compare each ingredients to the value in the ranges to determine if the ingredient is safe, and if it is count it and remove it from future comparisons to prevent double counting.
    """
    total = 0

    # Seperate ranges and ingrediants from this input

    # Convert a string representation of a list of ranges, from the first part of this puzzle
    # for example:
    # 3-5
    # 10-14
    # 16-20
    # 12-18
    # ...
    #
    # into a python list of those same ranges:
    # [(3, 5), (10, 14), (16, 20), (12, 18)]
    ranges = [(int(r.split('-')[0]),int(r.split('-')[1])) for r in puzzle.strip().split('\n\n')[0].split('\n')]

    # Convert a python list of ingrediants
    ingredients = [int(i) for i in puzzle.strip().split('\n\n')[1].split('\n')]

    # since these ranges are too big to throw in a set, what we can do is iterate over 
    # every individual range using a stack to store which ingredients we are checking against
    for pair in ranges:

        # if we were to assign stack = ingredients python would only make a shallow copy,
        # which means poping from stack would also pop from ingredients, using copy.deepcopy()
        # allows us to create a deep copy of the ingredients
        stack = copy.deepcopy(ingredients)
        while len(stack) > 0:
            current = stack.pop()
            if pair[0] < current and pair[1] >= current:
                total += 1
                # every time we discover an ingredient is valid we can remove it from the original list
                ingredients.remove(current)

    return total

def part2(puzzle: str) -> int:
    """
    """
    total = 0

    ranges = [(int(r.split('-')[0]),int(r.split('-')[1])) for r in puzzle.strip().split('\n\n')[0].split('\n')]

    # our main goal with this is to remove duplicate ranges such as:
    # 16-20 and 12-18
    # which is in reality just 16-20
    # or
    # 10-16 and 12-18
    # which should become 10-18
    # or 
    # 16-24 and 12-18
    # which becomes 12-24

    # I'm guessin there's a very cleaver way to solve this using boolean algebra,
    # but I'm far too stoopid to figure out how to do that.
    # so instead we'll eliminate all overlaping ranges

    # we start by sorting based on the first value of the range
    ranges.sort()
    
    #initialize the stack with a sentinel value of (0,0) since 0 will always be lower than the ranges
    stack = [(0,0)]


    # merge the ranges by iterating over each possible range, extracting the minimum possible left value and the maximum possible right value removing any ranges that are enveloped by those left and right values using a stack
    for pair in ranges:
        left = pair[0]
        right = pair[1]

        # check existing ranges already on the stack
        for i in range(len(stack)):
            if pair[0] <= stack[i][1]:
                while len(stack) > i:
                    current = stack.pop()
                    left = min(current[0],left)
                    right = max(current[1],right)
        
        stack.append((left,right))

    #remove the (0,0) sentinel value we added to the start of the stack
    stack = stack[1:]

    # finally we can calculate the total sum of ranges by iterating over each pair and adding
    # pair[0] - pair[1] to the total
    for pair in stack:
        total += (pair[1] + 1) - pair[0]

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

    test_file = open('test1.txt','r')
    test_data = test_file.read()
    test_file.close()
