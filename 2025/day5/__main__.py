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

if __name__ == '__main__':
    test_file = open('test1.txt','r')
    test_data = test_file.read()
    test_file.close()

    print(f'part 1 - test 1 output : {part1(test_data)}')

    input_file = open('input1.txt','r')
    input_data = input_file.read()
    input_file.close()

    print(f'part 1 - output : {part1(input_data)}')
