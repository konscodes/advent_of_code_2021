from pathlib import Path

def corrupted(line, open):
    for symb in line:
        if symb in symbols.keys():
            open.append(symb)
        elif symb in symbols.values():
            if symbols[open[-1]] == symb:
                open.pop()
            else:
                return symb
    

def syntax_check(data):
    return [corrupted(line, list()) for line in data]


def total_syntax_error(data):
    return sum([syntax_check(data).count(char)*points for char, points in points.items()])


if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test10.txt'

    with open(file) as f:
        data = f.read().splitlines()
    
    symbols = {'(':')', '[':']', '{':'}', '<':'>'}
    points = {')':3, ']':57, '}':1197, '>':25137}
    print('part1: ', total_syntax_error(data))