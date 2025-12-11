"""
Advent of Code Day10
"""

import copy

def distance(current,target):
    n = len(target)
    total = 0

    for i in range(n):
        if current[i] != target[i]:
            total += 1

    return total

def press(button,state):
    new_state = state
    for change in button:
        if state[change] == '.':
            new_state = new_state[:change] + '#' + new_state[change+1:]
        else:
            new_state = new_state[:change] + '.' + new_state[change+1:]
    return new_state

def part1(machines: str) -> int:
    """
    """
    total = 0

    
    machine_list = []
    edge_list = []
    node_list = []
    unvisited_list = []


    for row in machines.strip().split('\n'):

        # break up the input
        machine = row.split(' ')[0][1:-1]
        off_state = '.' * len(machine)
        buttons = [[int (s) for s in b[1:-1].split(',')] for b in row.split(' ')[1:-1]]

    

        # for future use in djikstra's algroithm
        unvisited = set([off_state])

        # when this reaches 0 we know our program has found a solution.
        machine_distance = float('inf')

        edges = {}

        stack = [off_state]

        # Build an adjacency list of all possible connections using an algorithm similar to
        # dfs
        while len(stack) > 0:

            current = stack.pop()
            unvisited.add(current)

            for button in buttons:
                p = press(button,current)
                unvisited.add(p)
                if current not in edges:
                    edges[current] = [p]
                elif p not in edges[current]:
                    edges[current].append(p)
                    stack.append(p)
        machine_list.append(machine)
        edge_list.append(edges)
        node_list.append(set(list(edges)))
        unvisited_list.append(unvisited)

    #use djikstra's algorithm to find the minimum possible distance of the target endpoint
    for i in range(len(edge_list)):

        unvisited = list(unvisited_list[i])
        distances = dict()

        # set the distances of everything else to infinity
        for j in unvisited:
            distances[j] = float('inf')
        
        # ensure that the distance to the first value is zero
        blank = '.' * len(unvisited[0])

        distances[blank] = 0


        while len(unvisited) > 0:

            min_distance = float('inf')
            # set current to the minimum in distance away in unvisited
            current_index = float('-inf')
            for k, v in enumerate(unvisited):
                if distances[v] < min_distance:
                    min_distance = distances[v]
                    current_index = k
            current = unvisited.pop(current_index)

            if current in edge_list[i]:
                for neighbour in edge_list[i][current]:
                    delta = distances[current] + 1

                    if (neighbour in distances) and (delta < distances[neighbour]):
                        distances[neighbour] = delta


        #finally get the distance of each machine and add it to the total
        total += distances[machine_list[i]]

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
