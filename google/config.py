sentencePlace = []  # (file,row)

words = dict()

around_letter = {
    'a': ['q', 'w', 's', 'x', 'z'],
    'b': ['v', 'g', 'h', 'n'],
    'c': ['x', 'd', 'f', 'v'],
    'd': ['s', 'e', 'r', 'f', 'c', 'x'],
    'e': ['w', 's', 'd', 'f', 'r'],
    'f': ['d', 'r', 't', 'g', 'v', 'c'],
    'g': ['t', 'y', 'h', 'b', 'v', 'f'],
    'h': ['y', 'u', 'j', 'n', 'b', 'g'],
    'i': ['u', 'j', 'k', 'l', 'o'],
    'j': ['u', 'i', 'k', 'm', 'n', 'h'],
    'k': ['i', 'o', 'l', ',', 'm', 'j'],
    'l': ['p', 'o', 'k', ',', '.', ';'],
    'm': [',', 'k', 'j', 'n'],
    'n': ['m', 'j', 'h', 'b'],
    'o': ['p', 'l', 'k', 'i'],
    'p': ['o', 'l', ';', '['],
    'q': ['w', 's', 'a'],
    'r': ['e', 'd', 'f', 't'],
    's': ['a', 'w', 'e', 'd', 'x', 'z'],
    't': ['r', 'f', 'g', 'y'],
    'u': ['y', 'h', 'j', 'i'],
    'v': ['c', 'f', 'g', 'b'],
    'w': ['q', 'a', 's', 'e'],
    'x': ['z', 's', 'd', 'c'],
    'y': ['t', 'g', 'h', 'u'],
    'z': ['a', 's', 'x']
}
