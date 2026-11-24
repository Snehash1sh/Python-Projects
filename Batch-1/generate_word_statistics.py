def generate_word_statistics(text):
    txt = text.lower()
    l = list(txt.split())
    uniq_l = dict()
    lwc = 0
    lwci = ()
    swc = 0
    swci = ()
    len_e = list()
    print("Modular Word Statistics")
    print("Total Words: ",len(l))
    for i in l:
        if i not in uniq_l:
            uniq_l.update({i:1})
        else:
            uniq_l[i] +=1
        if len(i) > lwc:
            lwc = len(i)
            lwci = l.index(i)
            swc =  lwc
    for j in l:
        if 0 <= len(j) <= swc:
            swc = len(j)
            swci = l.index(j)
        len_e.append(float(len(i)))
    print(f"Unique Words: {len(uniq_l)}")
    print("Longest Words:",l[lwci].lower())
    print("Shortest Words:",l[swci])
    print("Average Word Length:",sum(len_e) // float(len(l)))
    return []
generate_word_statistics()
