# Part2 
from pathlib import Path
import pdb
path = Path(__file__).resolve()
parent = path.parent
file_path = parent / 'day8.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read()
        data = [i.split(' | ') for i in data.split(sep='\n')]
        #print(data)
    return data


def decode(input_data):
    one, seven, four, two, three, five, six, nine, zero, eight = [set(i) for i in sorted(input_data, key=len)]
    all_len_five = list(filter(lambda x:len(x)==5, input_data))
    all_len_six = list(filter(lambda x:len(x)==6, input_data))
    two = [set(i) for i in all_len_five if set(i).union(four) == eight]
    three = [set(i) for i in all_len_five if set(i).issuperset(seven)]
    five = [set(i) for i in all_len_five if set(i).issuperset(four.difference(one))]
    six = [set(i) for i in all_len_six if set(i).issuperset(five[0]) and not set(i).issuperset(one)]
    nine = [set(i) for i in all_len_six if set(i).issuperset(seven) and set(i).issuperset(four)]
    zero = [set(i) for i in all_len_six if set(i).symmetric_difference(eight).issubset(five[0])]
    return zero[0], one, two[0], three[0], four, five[0], six[0], seven, eight, nine[0]


def match(output_data):
    result = []
    for mixed_letters in output_data:
        result += [digits.index(digit) for digit in digits if set(mixed_letters) == digit]
    return result


def counter(decoded_digits):
    string = ''.join(map(str, decoded_digits))
    return int(string)


data = read_data(file_path)
totals = 0
for line in data:
    # Pass list of mixed letters and return the list of sets
    input_data = line[0].split(' ')
    output_data = line[1].split(' ')
    zero, one, two, three, four, five, six, seven, eight, nine = decode(input_data)
    digits = (zero, one, two, three, four, five, six, seven, eight, nine)
    # Get the digit from index of digits that match the output
    result = match(output_data)
    print(output_data, result)
    totals += counter(result)

print(f'Adding all of the output values produces {totals}')