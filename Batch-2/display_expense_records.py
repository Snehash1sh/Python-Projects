def display_expense_records(records):
    run = False
    l=()
    l= records.split( )
    n = int(l[0])
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
        print("No Category Amount Date")
        for i in range (0,n):
            print(i+1,cat[i],float(amt[i]),date[i])
    return
display_expense_records()
