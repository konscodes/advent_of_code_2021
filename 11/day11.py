from pathlib import Path

def energy_levels(data):
    return [([1], [2,3,1])]


def count_flashes(data):
    return [sum([x.count(0) for x in energy_levels(data)])]

if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test11.txt'

    with open(file) as f:
        data = f.read().splitlines()
    
    print('part1: ', sum(count_flashes(data)))