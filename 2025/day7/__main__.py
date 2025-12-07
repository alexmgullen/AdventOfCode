"""
Advent of Code Day7
"""

def part1(diagram: str) -> int:
    """
    Discover the number of diverging paths in a diagram that looks like this:

    .......S.......
    ...............
    .......^.......
    ...............
    ......^.^......
    ...............
    .....^.^.^.....
    ...............
    ....^.^...^....
    ...............
    ...^.^...^.^...
    ...............
    ..^...^.....^..
    ...............
    .^.^.^.^.^...^.
    ...............

    Fig.1

    where 'S' is the start and '^' indicates a location where a beam sent from 'S' - as visualized using '|' - will be split into two seperate beams at the right and left of that '^' symbol, for example:

    .......S.......
    .......|.......
    ......|^|......
    ......|.|......

    Fig.2

    This function calclates the number of times a split occures in this diagram using by counting the number of splits that go into a splitter. In Fig.2 there would be one total split, dentoed by the '@' symbol in Fig.3:

    .......S.......
    .......|.......
    ......|@|......
    ......|.|......

    Fig.3

    In Fig.1 we have a grand total of 21 splits, denoted by the '@' symbol in Fig.4:

    .......S.......
    .......|.......
    ......|@|......
    ......|.|......
    .....|@|@|.....
    .....|.|.|.....
    ....|@|@|@|....
    ....|.|.|.|....
    ...|@|@|||@|...
    ...|.|.|||.|...
    ..|@|@|||@|@|..
    ..|.|.|||.|.|..
    .|@|||@||.|.@|.
    .|.|||.||.|..|.
    |@|@|@|@|^|.|@|
    |.|.|.|.|.|.|.|

    Fig.4

    NOTE: notice how (9,2) of this row wasn't hit by a beam so it doesn't count as split and remains a '^'

    Counting all the '@' symbols which represent the place where a beam was split results in 21, wich is the same as the output of this function for the same problem.
    """
    total = 0

    start = (-1,-1)
    splitters = []

    height = 0
    width = 0

    # useless for solving the actual problem, but helpful for visualization
    display = []

    # get the real location of start and the coordinates of all the splitters
    # we also use this double for loop to build the display
    for y, row in enumerate(diagram.strip().split('\n')):

        display_row = []
        for x, col in enumerate(row):
            if col == 'S':
                start = (x,y)
            elif col == '^':
                splitters.append((x,y))
            width = x # save the width for later, (the loop will always end with x at the width of the input)

            display_row.append(col) # visualization logic

        height = y # save the height for later, (the loop will always end with y at the height of the input)

        display.append(display_row) # display logic

    # create a list of places that the *tachyon* beam has been so we can determine
    # if the next space should be replaced by a *tachyon* beam
    path = [start]


    # simulate the problem, not that this is not efficient at all, especially 
    # since we are using a list for a path rather than a set, but it's good 
    # enough to get this problem solved.
    for y in range(height):
        s = 0
        for x in range(width):
            # check if this location is part of the path by seeing if the same location with a y of 1 less is in our current path
            if (x, y - 1) in path:

                # check if the current location is a splitter
                if (x,y) in splitters:
                    s += 1
                    display[y][x] = '@'
                    # if it is add the location to the right and left of the splitter to the path, as long as they are not already there
                    if (x-1,y) not in path:
                        path.append((x-1,y))
                        display[y][x-1] = '|'

                    if (x+1,y) not in path:
                        path.append((x+1,y))
                        display[y][x+1] = '|'

                else:
                    # if the location is not a splitter add this location to the path
                    path.append((x,y))

                    # we also replace the character in the display for visualization purposes
                    display[y][x] = '|'

            # print(display[y]) # uncomment for visualization of final output
        total += s

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
