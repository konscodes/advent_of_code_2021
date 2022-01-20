from pathlib import Path

def syntax_check(line, open):
    corrupted = False
    for symb in line:
        if symb in symbols.keys():
            open.append(symb)
        elif symb in symbols.values():
            if symbols[open[-1]] == symb:
                open.pop()
            else:
                corrupted = True
                return symb
                #break
    #return open, symb, corrupted
    

def corrupted(data):
    return [syntax_check(line, list()) for line in data]
    #return [[symb for open, symb, corrupted in syntax_check(line, list()) if corrupted == True] for line in data]


def total_syntax_error(data):
    return sum([corrupted(data).count(char)*points for char, points in corruption_points.items()])


def complition_scores(data):
    return sorted([10,20,30])


def middle_score(data):
    return complition_scores(data)[int(len(complition_scores(data)) / 2)]


if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test10.txt'

    with open(file) as f:
        data = f.read().splitlines()
    
    symbols = {'(':')', '[':']', '{':'}', '<':'>'}
    corruption_points = {')':3, ']':57, '}':1197, '>':25137}
    incomplete_points = {')':1, ']':2, '}':3, '>':4}
    print('part1: ', total_syntax_error(data))
    print('part2: ', middle_score(data))