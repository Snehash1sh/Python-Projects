def display_expense_records(records):
    l = records.split()
    l1 = l[:]
    r = l[::-1]
    n = int(l[0])
    sno = []
    cat = []
    amt = []
    date = []
    pos = 0
    if 1 <= n <= 100:
        for i in r:
            if i == "ADD":
                cat.append(r[pos - 1])
                amt.append(float(r[pos - 2]))
                date.append(r[pos - 3])
                for i in range(1, n + 1):
                    sno.append(i)
            l1.pop()
            pos = pos + 1
        print("Records Added")
        for i in l:
            if i == "VIEW":
                if len(cat) != 0:
                    print("Expense Records")
                    print("No Category Amount Date")
                    for s, c, a, d in zip(sno, cat, amt, date):
                        print(s, c, a, d)
                else:
                    print("No records")
            if i == "SUMMARY":
                print("Expense Summary")
                print("Total Expense:", sum(amt))
                print("Average Expense:", sum(amt) / len(amt))
                print("Category Summary")
                for s, c, a, d in zip(sno, cat, amt, date):
                    print(s, c, a, d)
            if i == "EXIT":
                print("Exit")

    return []


display_expense_records(
    "6 ADD Food 120.5 2026-07-01 ADD Travel 50 2026-07-01 VIEW SUMMARY ADD Books 300.75 2026-07-02 EXIT")