import os
from os import walk
from config import words, sentencePlace


def initalize():
    """
    Insert all the word in archive directory to hash map.
    Every word with all it appearance in the directory.

    """

    pathdir = os.getcwd() + "\Archive"
    dir_queue = [pathdir]
    while len(dir_queue) != 0:
        # with open(dir_queue[0]) as f:
        #     if dir_queue[0].
        #         from os import walk

        directory_path = dir_queue[0]
        for (dirpath, dirnames, filenames) in walk(directory_path):
            # print(directory_path,dirpath,filenames)
            for Dirname in dirnames:
                path = dirpath + '\{}'.format(Dirname)
                dir_queue.append(path)
            for Filename in filenames:
                filepath = dirpath + '\{}'.format(Filename)
                with open(filepath, encoding="utf8") as f:
                    # print(filepath)
                    text = f.readlines()
                    # print(text)
                    for line in text:
                        words_in_line = line.split()
                        for word in words_in_line:
                            file = filepath
                            row = text.index(line)
                            index_in_row = words_in_line.index(word)
                            sentencePlace.append((file, row, index_in_row))
                            if words.get(word) is None:
                                words[word] = ([len(sentencePlace) - 1])
                            else:
                                words.get(word).append(len(sentencePlace) - 1)

        # print(dir_queue)
        dir_queue.pop(0)
