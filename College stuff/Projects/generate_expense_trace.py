def generate_expense_trace(records, threshold):
    run = False
    l=()
    l= records.split( )
    n = int(l[0])
    sno = []
    s_cat = []
    threshold_val = []
    for i in range(1,n+1):
        sno.append(i)
    if 1<=n<=100:
        cat = (l[1:(len(l)):3])
        amt = (l[2:(len(l)):3])
        for i in amt:
            if 0<float(i)<=float(threshold):
                s_cat.append("Low")
            elif float(threshold)<float(i)<=1000:
                s_cat.append("Medium")
            else:
                s_cat.append("High")
            if 1<= float(i) <= 1000000:
                date = (l[3:(len(l)):3])
                run = True
            else:
                print("Invalid amount")
                run = False
                break
        for j in s_cat:
            if j != "Low":
                threshold_val.append("Above Threshold")
            else:
                threshold_val.append("Below Threshold")
        if run == True:
            sum_amt = 0
            for z in amt:
                sum_amt = sum_amt+float(z)
            print("Expense Tracker Trace")
            print("Input Records")
            print("No Category Amount Date")
            for i in range (0,n):
                print(i+1,cat[i],float(amt[i]),date[i])
            print("Processing Details")
            for i in range (0,n):
                print(f"Record {i+1} {cat[i]} | {s_cat[i]} | {threshold_val[i]} ")
            print("Final Summary")
            print("Total Expense:",sum_amt)
            print("Average Expense:",sum_amt/len(amt))
            print("Category Summary")
            for s, c, a, d in zip(sno,cat,amt,date):
                print(s,c,a,d)
            print("Above Threshold Expenses")
            for s, c, a, d in zip(sno,cat,amt,date):
                if float(a) >= 500:
                    print(s,c,d)
    return []
generate_expense_trace()