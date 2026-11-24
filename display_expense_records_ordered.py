def display_expense_records_ordered(records):
    l = records.split()
    n = int(l[0])

    if not (1 <= n <= 100):
        print("Invalid numbering")
        return

    cats = l[1::3]
    amts = [float(x) for x in l[2::3]]

    if any(not (0 <= a <= 1000000) for a in amts):
        print("Invalid amount")
        return

    total = sum(amts)
    average = total / n

    summary = {}
    for c, a in zip(cats, amts):
        summary[c] = summary.get(c, 0.0) + a

    print(f"Total Expense: {total:.2f}")
    print(f"Average Expense: {average:.2f}")
    print("Category Summary")
    for c in sorted(summary):
        print(f"{c} {summary[c]:.2f}")


display_expense_records_ordered()