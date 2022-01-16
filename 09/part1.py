from pathlib import Path

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


if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test9.txt'

    with open(file) as f:
        data = f.read().splitlines()
    
    print('part1: ', total_risk(data))