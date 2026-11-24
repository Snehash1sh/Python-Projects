def calculate_expense_summary(records):
    run = False
    l=()
    uniq=[]
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
    for i in cat:
        if i not in uniq:
            uniq.append(i)
    if run == True:
        print("No Category Amount Date")
        for i in range (0,n):
            print(i+1,cat[i],float(amt[i]),date[i])
    print(uniq)
    return
calculate_expense_summary()