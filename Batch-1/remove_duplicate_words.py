def remove_duplicate_words(words):
    l = list()
    l1 =words
    x = l1.split()
    dup_word_count = 0
    for i in x:
        i = i.lower()
        l.append(i)
    print("Duplicate Word Removal Report")
    print("Total number of words: ",len(l))
    uniq_list = list()
    for i in l:
        if i not in uniq_list:
            uniq_list.append(i)
        else:
            dup_word_count = dup_word_count + 1
    print("Duplicate Removed: ",dup_word_count)
    print("Unique Words: ",len(uniq_list))
    print("Unique Words List")
    print(*uniq_list)
    return []

remove_duplicate_words()
