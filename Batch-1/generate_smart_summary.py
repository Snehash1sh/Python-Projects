def generate_smart_summary(text, records):
    txt = text.lower()
    l = list(txt.split())
    uniq_l = dict()
    lwc = 0
    lwci = ()
    print("Smart Summary Report")
    print("Text Summary")
    print("Total Words: ",len(l))
    for i in l:
        if i not in uniq_l:
            uniq_l.update({i:1})
        else:
            uniq_l[i] +=1
        if len(i) > lwc:
            lwc = len(i)
            lwci = l.index(i)
    print(f"Unique Words: {len(uniq_l)}")
    print("Longest Words:",l[lwci].lower())
    print("Student Summary")
    n = int(records)
    rollno = []
    name = []
    marks = []
    status = []
    marks_2f = []
    passed = 0
    failed = 0
    sum1 = 0
    for i in range(n):
        var = input("Enter Details: ")
        l = var.split(" ")
        rollno.append(l[0])
        name.append(l[1])
        marks.append(l[2])
    for x in marks:
        marks_2f.append((f"{float(x):.2f}"))
    for y in marks_2f:
        if float(y) <= 40.00:
            status.append("Fail")
        else:
            status.append("Pass")
    for z in marks_2f:
        if float(z) >= 40:
            passed += 1
        else:
            failed += 1
        sum1 = sum1 + float(z)
    highest = marks_2f.index(max(marks_2f))
    print("Summary")
    print(f"Total Students: {n}")
    print(f"Passed {passed}")
    print(f"Failed {failed}")
    print(f"Average Marks:",sum1/n)
    print(f"Highest Scorer: {name[highest]} {marks[highest]}")
    return []
generate_smart_summary()
