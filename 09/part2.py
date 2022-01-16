from pathlib import Path
from itertools import islice
from math import prod
from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Runtime is {round(t2 - t1, 2)}s')
        return result
    return wrapper


def is_valid_position(data, i, j):
    return i >= 0 and i < len(data) and \
           j >= 0 and j < len(data[0])


def neighbors(data, i, j):
    return [(i+x, j+y) for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                       if is_valid_position(data, i+x, j+y)]


def low_point(data, i, j):
    return all(data[i][j] < data[x][y] 
                for x,y in neighbors(data, i, j))


def low_points(data):
    return [(i,j)
            for i in range(len(data))
            for j in range(len(data[0]))
            if low_point(data, i, j)]


def risk_levels(low_points):
    return [int(data[i][j]) + 1 for i,j in low_points]


def total_risk(data):
    return sum(risk_levels(low_points(data)))


def grow_basin(data, i, j, basin):
    basin.add((i, j))
    for x, y in neighbors(data, i, j):
        if data[x][y] > data[i][j] and data[x][y] < '9':
            grow_basin(data, x, y, basin)
    return basin


@performance
def basin_size(data):
    lows = low_points(data)
    basins = list()
    for low in lows:
        basin = grow_basin(data, *low, set())
        basins.append(len(basin))
    return prod(sorted(basins)[-3:])


if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'day9.txt'

    with open(file) as f:
        data = f.read().splitlines()
    
    print('part1: ', total_risk(data))
    print('part2: ', basin_size(data))
