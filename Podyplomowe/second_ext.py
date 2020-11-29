def make_pair(a, b):
    return [a, b]


def area_shape(a: int, b: int, shape: str):
    if shape == 'triangle':
        return 1 / 2 * (a * b)
    elif shape == 'parallelogram':
        return a * b
    else:
        print('Choose triangle or parallelogram')


def first_last(table):
    return [table[0], table[len(table)-1]]
