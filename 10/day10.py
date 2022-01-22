from pathlib import Path
from statistics import median

def syntax_check(line, chunk):
    corrupted = False
    for symb in line:
        if symb in symbols.keys():
            chunk.append(symb)
        elif symb in symbols.values():
            if symbols[chunk[-1]] == symb:
                chunk.pop()
            else:
                #corrupted = True
                #break
                return {'corrupted_symb': symb}
    #return [(open, symb, corrupted)]
    return {'incomplete_chunk': reversed(chunk)}


def corrupted(data):
    return [syntax_check(line, list()).get('corrupted_symb') for line in data]


def incomplete(data):
    return [syntax_check(line, list()).get('incomplete_chunk') for line in data]


def total_syntax_error(data):
    return sum([corrupted(data).count(char)*points for char, points in corruption_points.items()])


def total_score(chunk):
    score = 0
    for value in chunk:
        score *= 5
        score += incomplete_points[value]
    return score


def complition_scores(data):
    return [total_score(chunk) for chunk in incomplete(data) if chunk]


def middle_score(data):
    return median(complition_scores(data))


if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test10.txt'

    with open(file) as f:
        data = f.read().splitlines()
    
    symbols = {'(':')', '[':']', '{':'}', '<':'>'}
    corruption_points = {')':3, ']':57, '}':1197, '>':25137}
    incomplete_points = {'(':1, '[':2, '{':3, '<':4}
    print('part1: ', total_syntax_error(data))
    print('part2: ', middle_score(data))