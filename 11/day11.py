from pathlib import Path

def outbreak(flashes, neighbors):
    # loop through each neighbor [(x,y), (x,y)]
    # for each (x,y)
    #   check if 9 ->>
    #       set to 0
    #       increment flashes[0] += 1
    #       call outbreak(flashes, neighbors(i,j))
    #   else increment data[x][y]
    return 0


def energy_levels(data):
    flashes = [0]
    # loop through grid indexes i,j
    # for each i,j 
    #   check if 9 ->> 
    #       set to 0
    #       increment flashes[0] += 1
    #       call outbreak(flashes, neighbors(i,j))
    #   else increment data[i][j]
    return flashes[0]


def count_flashes(data):
    total = 0
    for i in range(1):
        print(i)
        total += energy_levels(data)
    return total
        

if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test11.txt'

    with open(file) as f:
        data = f.read().splitlines()
        data = [[int(y) for y in x] for x in data]
    
    print('part1: ', count_flashes(data))