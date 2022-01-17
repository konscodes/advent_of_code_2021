from pathlib import Path

def syntax_check(data):
    return [')']


def total_syntax_error(data):
    return sum([syntax_check(data).count(symbol)*points for symbol, points in close_symbol])


if __name__ == '__main__':
    path = Path(__file__).resolve()
    file = path.parent / 'test10.txt'

    with open(file) as f:
        data = f.read().splitlines()
    
    open_symbol = [')',']','}','>']
    #close_symbol = {')': 3,']': 57,'}': 1197,'>': 25137}
    close_symbol = [(')',3), (']',57), ('}',1197), ('>',25137)]
    print('part1: ', total_syntax_error(data))