def generate_daily_report(records):
    l = records.split()
    n = int(l[0])

    if n < 1 or n > 100:
        print("Invalid numbering")
        return

    cat = l[1::3]
    amt = l[2::3]
    date = l[3::3]

    expenses = {}

    for i in range(n):
        a = float(amt[i])
        if a < 0 or a > 1000000:
            print("Invalid amount")
            return

        d = date[i]
        if d not in expenses:
            expenses[d] = []
        expenses[d].append((cat[i], a))

    print("Daily Expense Report")
    for d in sorted(expenses):
        print("Date:", d)
        total = 0
        for item in expenses[d]:
            print(item[0], "{:.2f}".format(item[1]))
            total = total + item[1]
        print("Total:", "{:.2f}".format(total))


generate_daily_report()