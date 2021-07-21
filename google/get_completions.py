from config import words, sentencePlace


def get_completions(prefix: str):  # -> List[AutoCompleteData]
    lst = prefix.split(' ')
    lst = [i for i in lst if i != '']
    lst_indexes = [words[i] if i in words.keys() else [] for i in lst]

    best_k_completions = [(sentencePlace[i], 2 * len(lst[0])) for i in lst_indexes[0]]
    # for i in range(len(lst)):
    #     best_k_completions.append((lst_indexes[i], 2 * len(lst[i])))
    temp = []
    for word_ind in range(1, len(lst)):
        for index_1 in range(len(best_k_completions)):
            for index_2 in range(len(lst_indexes[word_ind])):
                if best_k_completions[index_1][0][0] == sentencePlace[lst_indexes[word_ind][index_2]][0] and \
                        best_k_completions[index_1][0][2] + 1 == sentencePlace[lst_indexes[word_ind][index_2]][2] and \
                        best_k_completions[index_1][0][1] == sentencePlace[lst_indexes[word_ind][index_2]][1]:
                    temp.append((sentencePlace[lst_indexes[word_ind][index_2]],
                                 best_k_completions[index_1][1] + len(lst[word_ind]) + 1))
        # if len(temp) < 5:
        #     for _ in range(5 - len(temp)): pass

        best_k_completions = temp

    return best_k_completions
