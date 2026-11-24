def process_student_records(record):
    n = int(record)
    l =[]
    rollno = []
    name = []
    marks = []
    status = []
    marks_2f = []
    passed = 0
    failed = 0
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
    print("Student Records")
    print("Roll Name Marks Status")
    highest = marks_2f.index(max(marks_2f))
    for i in range(n):
        print(rollno[i], name[i], marks_2f[i], status[i])
    print("Summary")
    print(f"Total Students: {n}")
    print(f"Passed {passed}")
    print(f"Failed {failed}")
    print(f"Highest Scorer: {name[highest]} {marks[highest]}")
    return []
process_student_records(5)