"""
Advent of Code Day4
"""

def part1(diagram: str) -> int:
    """
    Transform the diagram into an array, find all the '@' symbols on that array and add them to a stack, then  count the number of neighbouring '@' symbols each of those '@' symbols have and return the total amount of '@' symbols that have less than 4 '@' neighbours.
    """
    total = 0
    limiting_rolls = 4

    # we'll need to know the these values for boundary checking later so it's worth computing them now.
    y_max = len(diagram.strip().split('\n'))
    x_max = len(diagram.split('\n')[0])

    # transform the diagram from a string with newlines into an array
    # the "[::-1]" in the first comprehension is to ensure that the point 0,0 is in the bottom left, this is not strictly necesary, and might add a bit of obfuscation to the logic of this program, but I wanted to make it match the coordinates of a cartesean plane, so here we are.
    # Example
    # 9 - . . @ @ . @ @ @ @ .
    # 8 - @ @ @ . @ . @ . @ @
    # 7 - @ @ @ @ @ . @ . @ @
    # 6 - @ . @ @ @ @ . . @ .
    # 5 - @ @ . @ @ @ @ . @ @
    # 4 - . @ @ @ @ @ @ @ . @
    # 3 - . @ . @ . @ . @ @ @
    # 2 - @ . @ @ @ . @ @ @ @
    # 1 - . @ @ @ @ @ @ @ @ .
    # 0 - @ . @ . @ @ @ . @ .
    #     | | | | | | | | | |
    #     0 1 2 3 4 5 6 7 8 9
    #
    # NOTE: All this is theoretically uncessesay since we could just create a simple function to resolve a (x,y) coordinate to a location on the string and vise versa, but this is simpler for me.
    rolls = [list(x) for x in [y for y in diagram.strip().split('\n')[::-1]]]

    stack = []
    # get all the '@' symbols and add them to the stack, we use y_max and x_max since they've already been computed
    for y in range(y_max):
        for x in range(x_max):
            if rolls[y][x] == '@':
                stack.append((y,x)) # NOTE: this should probably be (x,y) mathematically speaking, but to simplify the logic I'm going to use (y,x).

    # store the 8 directions we want to check in
    directions = [
            (-1, 1),( 0, 1),( 1, 1),
            (-1, 0),        ( 1, 0),
            (-1,-1),(0, -1),( 1,-1)
    ]


    # perform a 'half BFS' to find the number of nearby neighbours
    for point in stack:
        neighbours = 0

        # check all eight directions
        for direction in directions:
            dy = point[0] + direction[0]
            dx = point[1] + direction[1]
            # boundary checking to make sure we don't try to index a value off the diagram/array
            if (dx >= x_max or dx < 0) or (dy >= y_max or dy < 0):
                pass
            elif rolls[dy][dx] == '@':
                neighbours += 1

        # if number of neighbours is less more than 'limiting_rolls' add one to the  total
        if neighbours < 4:
            total += 1

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
