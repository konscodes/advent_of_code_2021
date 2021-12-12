# Part1
from pathlib import Path

path = Path(__file__).resolve()
parent = path.parent
file_path = parent / 'day7.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read().split(sep=',')
        data = [int(i) for i in data]
    return data


data = read_data(file_path)
available_space = list(range(max(data) + 1))
total_cost = [0 for i in range(len(available_space))]
#print(available_space)
for position in data:
    #print(position)
    distance = [abs(position - i) for i in available_space]
    #print(distance)
    cost = [int((n*(n+1))/2) for n in distance]
    #print(cost)
    total_cost = [a + b for a, b in zip(total_cost, cost)]
    #print(total_cost)

print(f'Min fuel {min(total_cost)} in position {total_cost.index(min(total_cost))}')