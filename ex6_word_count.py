def word_count(s):
    word_dic = {}
    for word in s.split():
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    return word_dic