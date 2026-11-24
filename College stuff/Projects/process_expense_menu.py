def process_expense_menu(commands):
    output = []
    items = []

    cats = []
    amts = []
    dates = []

    j = commands.split()
    items.append(j)
    for command in items:

        if command == "ADD":
            cats.append(parts[1])
            amts.append(float(parts[2]))
            dates.append(parts[3])
            output.append("Record Added")

        elif command == "VIEW":
            output.append("Expense Records")
            if len(cats) == 0:
                output.append("No records")
            else:
                output.append("No Category Amount Date")
                for i in range(len(cats)):
                    output.append(str(i + 1) + " " + cats[i] + " " + "{:.2f}".format(amts[i]) + " " + dates[i])

        elif command == "SUMMARY":
            output.append("Expense Summary")
            if len(cats) == 0:
                output.append("No records")
            else:
                total = sum(amts)
                average = total / len(amts)
                output.append("Total Expense: " + "{:.2f}".format(total))
                output.append("Average Expense: " + "{:.2f}".format(average))
                output.append("Category Summary")

                for c in sorted(set(cats)):
                    cat_total = 0
                    for i in range(len(cats)):
                        if cats[i] == c:
                            cat_total = cat_total + amts[i]
                    output.append(c + " " + "{:.2f}".format(cat_total))

        elif command == "EXIT":
            output.append("Exit")


    print()

    return

process_expense_menu("6 ADD Food 120.5 2026-07-01 ADD Travel 50 2026-07-01 VIEW SUMMARY ADD Books 300.75 2026-07-02 EXIT SUMMARY")