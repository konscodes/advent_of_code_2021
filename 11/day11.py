from pathlib import Path

def energy_levels(data):
    return {'modified': [[1], [2,3,1]], 'flashes': 10}


def count_flashes(data):
    total = 0
    for i in range(100):
        iteration = energy_levels(data)
        total += iteration['flashes']
        data = iteration['modified']
    return total
        

if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test11.txt'

    with open(file) as f:
        data = f.read().splitlines()
    
    print('part1: ', count_flashes(data))