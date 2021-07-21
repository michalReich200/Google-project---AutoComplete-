from get_completions import get_completions
from veriations import get_all_variations


def get_best_5_completions(prefix: str):
    lst = get_completions(prefix)
    # # if len(lst) >= 5:
    # #     return [lst[i] for i in range(min(5, len(lst)))]
    # score = 0
    # while (len(lst) < 5):
    #     score += 1
    #     veriation = get_all_variations(prefix, score)
    #     for i in veriation:
    #         lst += get_completions(i)
    # return [lst[i] for i in range(min(5, len(lst)))]
    return lst
