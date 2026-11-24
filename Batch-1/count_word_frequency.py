def count_word_frequency(words):
    n =int(words)
    words2 = {}
    words1 = input("Enter your words: ")
    l = list(words1.split( ))
    l1 = list()
    for j in l:
        l1.append(j.lower())
    for i in l1:
        words2.update({i:l1.count(i)})
    print("Word Frequency Report")
    for k in words2:
        print(k,words2[k])
    return []
count_word_frequency(8)
