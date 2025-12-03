"""
Advent of Code Day3
"""

def part1(batteries: str) -> int:
    """
    This is a simulation solution to this problem which uses two pointers to manually find the maximum value.
    """
    # the ": str" and "->" are type annotation in python 3, they provide some weak typing that enforces that the "batteries" input is a string (batteries: str) and that the output of the function is an integer (-> int)
    total = 0

    # each battery is on a new line, we want to iterate over each battery so we can split based on that newline
    for row in batteries.split('\n'):

        # there is a newline before the end of the input which makes python think there is one last line even if the content of this line is "", this if function checks if the length is zero and if it is it doesn't run the logic to prevent our code from tying to index out of bounds (which would be anywhere on an array that is of length 0, (you can't even index zero on a "[]"))
        if len(row) > 0:
            row_total = 0
            # turn the batteries into an array of characters
            battery = [row[i] for i in range(len(row))]

            # use two pointers to iterate over every number combination in the array
            # initialize a left "pointer" (l) and a right "pointer" (r) at the first and second indexes
            l, r = 0, 1

            # the right pointer is going to iterate over every number before the on the array
            while r < len(battery):

                # the left pointer is going to iterate over every number up to the right pointer only
                while l < r:
                    # concatenate the number characters (so '1' + '2' becomes '12' instead of '3')
                    # then check if that value is greater
                    row_total = max(int(battery[l] + battery[r]),row_total)

                    # incrementation logic for the left pointer
                    l += 1

                # incrementation logic for the right pointer 
                l = 0
                r += 1
            
            # add the highest number in this row to the overall toal
            total += row_total

    #return the total as a number
    return total

def part2(batteries: str) -> int:
    """
    This is the same problem as part 1 except now instead of getting just this first and second, we need to find the first 12 characters. Since this would require 12 pointers to solve using the same method as part1 we'll instead take a greedy approach,

    Step 1 is to get the largest number that is as far to the left as possible since that will always produce the largest number, not that beacause the minimum size of our array is 12, we have to start at the 12th index so that our array is a minimum of 12 long.

    in this visual the number underneath our input is a mask where "1" represents a number that is selected for our final value, and "X" represent's a spot we simply can't use.


    987654321111111
    1000XXXXXXXXXXX = 9


    811111111111119
    1000XXXXXXXXXXX = 8


    234234234234278
    0010XXXXXXXXXXX = 4


    818181911112111
    1000XXXXXXXXXXX = 8

    Now we can continue reduce the inaccessible area by one since we now only have 11 spaces to fill, and do the same thing for the second value:

    987654321111111
    11000XXXXXXXXXX = 98


    811111111111119
    11000XXXXXXXXXX = 81

    234234234234278
    XX101XXXXXXXXXX = 42  - the values after 4 are locked since we don't want to override 4 as our highest

    818181911112111
    10100XXXXXXXXXX = 88

    and we can continue like this when we only have 10 spaces left in our battery:

    987654321111111
    111000XXXXXXXXX = 987


    811111111111119
    111000XXXXXXXXX = 811

    234234234234278
    XX1011XXXXXXXXX = 424

    818181911112111
    1X1010XXXXXXXXX = 888

    this can be continued all the way until battery size is zero, at which point we have our solution.

    987654321111111
    111111111111000 = 987654321111

    811111111111119
    111111111110001 = 811111111119

    234234234234278
    XX1X11111111111 = 424234234278

    818181911112111
    1X1X1X111111111 = 888911112111

    (An awesome part of AOC problems is that they sometimes encourage you to build solutions to part1 that scale to part2, for example if we'd built this and sent the parameters to 2 earlier we would already have had this part complete, and it would possibly have been a more scalable solutions for this problem)
    """
    total = 0
    battery_size = 12

    # this is another way to deal with tailing whitespaces, simply remove them before we split the string using the '.strip()' function. this remove the need for an if statement which can sometimes help the logic of our program
    for row in batteries.strip().split('\n'):

        #turn the array into an array of integers
        battery = [int(row[i]) for i in range(len(row))]

        # step 1, grab the largest number that is as far, or further than the max battery size
        first  = 0

        # start at the right and iterate over the battery in reverse
        for i in range(len(battery) - battery_size, 0 -1,-1):
            # greater than or equal to since we want to find the furthest one to the left
            if battery[i] >= battery[first]:
                #set first to be the index of the first largest value
                first = i

        # step 2 do the same thing for every other element until we have a stack full of the highest numbers

        # this stack stores indeces only to allow us to use those indeces as boundaries
        stack = [first]

        while len(stack) < battery_size:

            # set r to the the first "unlocked" index
            r = len(battery) - (battery_size - len(stack))

            # give higest a sentinel value to start
            highest = -1
            
            # iterate from right to left until we reach the last value we selected
            while r > stack[-1]:

                # if highest is the sentinel value or higher than the last highest value set the index of highest to be the current index
                if highest == -1 or battery[r] >= battery[highest]:
                    highest = r
                r -= 1

            # add the highest overall in our available list to the stack
            stack.append(highest)

        # this effectively takes our stack of indeces, converts them back to values and joins them into a string
        s_value = ''.join([str(battery[i]) for i in stack])

        
        total += int(s_value)

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
