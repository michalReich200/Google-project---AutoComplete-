def get_sentence(file, raw):
    with open(file) as file:
        lst = file.read()
        lst = lst.split('\n')
        return lst[raw]
