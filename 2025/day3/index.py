"""
Advent of Code Day3
"""

def part1(batteries: str) -> int:
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


if __name__ == '__main__':
    test_file = open('test1.txt','r')
    test_data = test_file.read()
    test_file.close()

    print(f'part 1 - test 1 output : {part1(test_data)}')

    input_file = open('input1.txt','r')
    input_data = input_file.read()
    input_file.close()

    print(f'part 1 - output : {part1(input_data)}')
