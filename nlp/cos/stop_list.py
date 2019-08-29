import os
def stop_list():
    stop_list = set()
    with open(os.path.join("./../cos/","stop_list.txt"), 'r', encoding='utf-8') as f:
        for word_lst in f.readlines():
            word = word_lst[0]
            stop_list.add(word)
    return stop_list
