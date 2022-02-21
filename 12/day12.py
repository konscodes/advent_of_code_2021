from pathlib import Path

def locate_path(entry, caves, path):
    for cave in caves[entry]:
        if cave in path and cave[0].islower():
            continue
        else:
            path.append(cave)
            return path if cave == 'end' else locate_path(cave, caves, path)
    return path
# Locate path works for a single path. How to find all possible paths?

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

def cave_connections(data, caves):
    for pair in data:
        if pair[0] not in caves:
            caves[pair[0]] = []
        caves[pair[0]].append(pair[1])
        if pair[1] not in caves:
            caves[pair[1]] = []
        caves[pair[1]].append(pair[0])
    return caves

if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test12.txt'
    pairs = read_data(file)
    caves = cave_connections(pairs, {})
    print(locate_path('start', caves, ['start']))
    print('part1: ', locate_all_pathways(caves))