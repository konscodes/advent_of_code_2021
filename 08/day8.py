# Part1
from pathlib import Path

path = Path(__file__).resolve()
parent = path.parent
file_path = parent / 'day8.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read()
        data = [i.split(' | ') for i in data.split(sep='\n')]
        input_data = [i[0] for i in data]
        output_data = [i[1] for i in data]
        print(output_data)
    return input_data, output_data


input_data, output_data = read_data(file_path)
counter = 0
for line in output_data:
    segment_list = line.split(' ')
    for segment in segment_list:
        counter += 1 if len(segment) <= 4 or len(segment) == 7 else 0
print(counter)
