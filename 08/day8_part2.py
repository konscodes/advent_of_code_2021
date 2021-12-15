# Part2 
from pathlib import Path

path = Path(__file__).resolve()
parent = path.parent
file_path = parent / 'test8.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read()
        data = [i.split(' | ') for i in data.split(sep='\n')]
        print(data)
    return data


def decode(input_data):
    one, four, seven, eight = [(),(),(),()]
    five = ()
    three = ()
    two = ()
    six = ()
    nine = ()
    zero = ()
    return zero, one, two, three, four, five, six, seven, eight, nine


data = read_data(file_path)
for line in data:
    # Pass list of mixed letters and return the list of sets
    input_data = line[0].split(' ')
    output_data = line[1].split(' ')
    zero, one, two, three, four, five, six, seven, eight, nine = decode(input_data)
    digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    
    # Get the digit from index of digits that match the output
    for mixed_letters in output_data:
        result = [digits.index(digit) for digit in digits if set(mixed_letters) in digit]
    print(output_data, result)