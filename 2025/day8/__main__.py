"""
Advent of Code Day8
"""

import math


class DisjointSet:
    parent = {}

    def make_set(self,universe):
        for i in universe:
            self.parent[i] = i

    def find(self,k):
        """
        Find the representative of the set 'k' belongs to
        """
        if self.parent[k] == k:
            return k
        else:
            return self.find(self.parent[k])

    def union(self,a,b):
        """
        Joint Set 'a' onto set 'b'
        """
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y

    def get_set(self):
        return self.parent



def distance_3d(p: tuple,q: tuple) -> int:
    """
    Gets the euclidean distance between points p and q in 3 dimensional space using this formula:
    https://en.wikipedia.org/wiki/Euclidean_distance#Higher_dimensions
    """
    # This is technically a reimplementation  of the math.dist(p,q) function in 
    # the math library, but I wanted to learn how to implement this myself, so here we go

    dx = (p[0] - q[0]) ** 2
    dy = (p[1] - q[1]) ** 2
    dz = (p[2] - q[2]) ** 2

    return math.sqrt(dx+dy+dz)


def part1(puzzle: str, connection_size: int) -> int:
    """
    """
    total = 1
    coordinates = []

    infinity_3d = (float('inf'),float('inf'),float('inf'))

    for row in puzzle.strip().split('\n'):
        # this could probably be done in a single line but I wanted to make 
        raw = row.split(',')
        x = int(raw[0])
        y = int(raw[1])
        z = int(raw[2])
        coordinates.append((x,y,z))

    # build out a list of all possible connections between coordinates including the distance of those coordinates
    connections = {}

    for l in coordinates:
        for r in coordinates:
            delta = distance_3d(l,r)
            if delta > 0 and (r,l) not in connections:
                connections[(l,r)] = delta

    shortest = sorted([d for d in connections.items()],key=lambda i: i[1])[:connection_size]


    # I was able to get up to this part before I had to stop and get help. Since this 
    # is a data structure I'd mostly forgotten about until now, but was just
    # reintorduced to today, Disjoint Sets 
    # https://www.techiedelight.com/disjoint-set-data-structure-union-find-algorithm/

    distinct = set()

    for coordinate in coordinates:
        distinct.add(coordinate)

    tree = DisjointSet()

    tree.make_set(list(distinct))

    for edge in shortest:
        tree.union(edge[0][0],edge[0][1])

    counts = {}

    for d in distinct:
        current = tree.find(d)
        if current in counts:
            counts[current] += 1
        else:
            counts[current] = 1

    stack = sorted([i for i in counts.items()],key=lambda j: j[1])

    for i in range(3):
        current = stack.pop()
        total *= current[1]

    return total


if __name__ == '__main__':
    test_file = open('test1.txt','r')
    test_data = test_file.read()
    test_file.close()

    print(f'part 1 - test 1 output : {part1(test_data,10)}')

    input_file = open('input1.txt','r')
    input_data = input_file.read()
    input_file.close()

    print(f'part 1 - output : {part1(input_data,1000)}')
