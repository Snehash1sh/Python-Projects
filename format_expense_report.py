def format_expense_report(records):
    run = False
    l=()
    l= records.split( )
    n = int(l[0])
    sno = []
    for i in range(1,n+1):
        sno.append(i)
    if 1<=n<=100:
        cat = (l[1:(len(l)):3])
        amt = (l[2:(len(l)):3])
        for i in amt:
             if 1<= float(i) <= 1000000:
                  date = (l[3:(len(l)):3])
                  run = True
             else:
                 print("Invalid amount")
                 run = False
                 break
    else:
        print("Invalid numbering")
        run = False
    if run == True:
        print("Formatted Expense Report")
        for s, c, a, d in zip(sno,cat,amt,date):
             newdate = d[8:10] + "-" + d[5:7]+ "-" + d[0:4]
             print(f"{s}. Category: {c.replace("_"," ").title()} | Amount: {a} | Date: {newdate}")
    return []
format_expense_report()