from pathlib import Path

script_path = Path(__file__).resolve()
script_parent = script_path.parent
data_file_path = script_parent / 'test9.txt'

def read_data(file_path):
    with open(file_path) as file_object:
        data = file_object.read()
        data = data.split(sep='\n')
        rows = [[int(x) for x in i] for i in data]
        columns = [[line[i] for line in rows] for i in range(len(rows[0]))]
    return rows, columns


def local_lows(entry):
    slide_left = entry[1:] + [entry[-1] + 1]
    slide_right = [entry[0]+1] + entry[:-1]
    return [i for i, j in enumerate(entry) if entry[i] < slide_left[i] and entry[i] < slide_right[i]]


def global_lows(rows, columns):
    low_map = [[0 for i, _ in enumerate(columns)] for x, _ in enumerate(rows)]
    row_lows = [local_lows(row) for row in rows]
    column_lows = [local_lows(column) for column in columns]
    print(row_lows)
    print(column_lows)
    for row, lows in enumerate(row_lows):
        for low in lows:
            low_map[row][low] += 1

    print(low_map)
    return low_points


rows, columns = read_data(data_file_path)
low_points = global_lows(rows, columns)
