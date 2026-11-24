def search_and_sort_students(records, search_roll):
    n = int(records)
    s_roll = int(search_roll)
    l = list()
    for i in range(n):
        x =input("Enter student data: ")
        x = x.split()
        l.append(x)
    print("Search Result")
    for rec in l:
        if str(rec[0]) == str(s_roll):
            print(rec[0],rec[1],rec[2])
    print("Sorted Records")
    print(f"Roll Name Records")
    for a in l:
        print(*a)
    return []
search_and_sort_students(,)
