from pathlib import Path

def is_valid_position(data, i, j):
    return i >= 0 and i < len(data) and \
           j >= 0 and j < len(data[0])


def neighbors(data, i, j):
    return [(i+x, j+y) for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1), 
                                    (-1, 1), (-1, -1), (1, -1), (1, 1)]
                        if is_valid_position(data, i+x, j+y)]


def outbreak(flashes, nearby):
    for a,b in nearby:
        if data[a][b] == 9:
            data[a][b] = 0
            flashes[0] += 1
            outbreak(flashes, neighbors(data, a,b))
        else: data[a][b] += 1
    return 0


def energy_levels(data):
    flashes = [0]
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 9:
                data[i][j] = 0
                flashes[0] += 1
                outbreak(flashes, neighbors(data, i,j))
            else: data[i][j] += 1
    [print(x) for x in data]
    print()
    return flashes[0]


def count_flashes(data):
    total = 0
    for i in range(2):
        total += energy_levels(data)
    return total
        

if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test11.txt'

    with open(file) as f:
        data = f.read().splitlines()
        data = [[int(y) for y in x] for x in data]
    
    print('part1: ', count_flashes(data))