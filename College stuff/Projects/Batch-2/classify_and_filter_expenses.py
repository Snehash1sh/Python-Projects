def classify_and_filter_expenses(records, threshold):
    run = False
    l=()
    l= records.split( )
    n = int(l[0])
    s_cat=[]
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
    else:
        print("Invalid numbering")
        run = False
    if run == True:
        print("Expense Classification")
        print("No Category Amount Date Class")
        for i in range (0,n):
            print(i+1,cat[i],float(amt[i]),date[i],s_cat[i])
        print("Above Threshold")
        for i in s_cat:
            if i == "Medium":
                print(cat[s_cat.index(i)],float(amt[s_cat.index(i)]),date[s_cat.index(i)])
            elif i == "High":
                print(cat[s_cat.index(i)],float(amt[s_cat.index(i)]),date[s_cat.index(i)])
    return
classify_and_filter_expenses()