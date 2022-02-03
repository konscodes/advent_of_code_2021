from pathlib import Path

def locate_path(entry, caves, path):
    return ['Path if it is valid and has reached an end']

def locate_all_pathways(caves):
    return [['List of pathways in a list']]

def read_data(file):
    '''
    Returns list of pairs in tuples
    '''
    with open(file) as f:
        data = f.read().splitlines()
        data = [tuple(x.split('-')) for x in data]
    return data

def cave_connections(data):
    return {'Each cave': 'And its connection'}

if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test12.txt'
    pairs = read_data(file)
    connections = cave_connections(pairs)
    print('part1: ', locate_all_pathways(connections))