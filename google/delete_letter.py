def delete_letter(str):
    lst = []
    for i in range(len(str)):
        lst.append(str[:i] + str[i + 1:])
    return lst
