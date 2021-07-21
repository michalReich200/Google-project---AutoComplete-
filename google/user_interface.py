from getSentence import get_sentence
from get_best_5_completions import get_best_5_completions
from initalize import initalize


def user_interface():
    print('Loading.....')
    initalize()
    print('Your text:')
    prefix = input()
    while 1:
        a = get_best_5_completions(prefix)
        for i in range(len(a)):
            print(f'{i+1}. {get_sentence(a[i][0][0], a[i][0][1])}')
            # print(f'{i}.  {a[i]}')
        prefix += input(prefix)
        while(prefix[-1]=='#'):
            print('Your text:')
            prefix = input()

