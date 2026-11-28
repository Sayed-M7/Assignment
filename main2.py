customers=["Ahmed","Sara","Omar","Mona","Ali","Nour","Youssef","Hana","Khalid","Mariam","Hassan","Laila"]
scores=[91,45,78,66,88,30,72,95,51,60,84,39]
risk_levels=[]
for name,score in zip(customers,scores):
    if score>=85:
       risk_level="High"
    elif score>=60:
       risk_level="Medium" 
    else:
        risk_level="Low"  
    risk_levels.append(risk_level)

print(risk_levels)   
High_num=0
Medium_num=0
Low_num=0
Total=0
for score,risk in zip(scores, risk_levels):
    Total=Total+score
    if risk=="High":
       High_num+=1
    elif risk=="Medium":
       Medium_num+=1
    else:
       Low_num+=1
The_average=Total/len(scores)
Worst_cust=customers[0]
lowest_score=scores[0]
Best_cust=customers[0]
highest_score=scores[0]
for name,score in zip(customers,scores):
    if score< lowest_score:
       Worst_cust=name
       lowest_score=score
    if score> highest_score:
        Best_cust=name
        highest_score=score
        choice=input("YOUR CHOICE IS ")
if choice =="1":
   print("CUSTOMER RISK REPORT")
   print()
   print("Name" , "Score" , "Risk" )
   for name,score,risk in zip(customers,scores,risk_levels):
      print(name,score,risk)
      print()
print("===== SUMMARY =====")
print()
print(f"High:{High_num}")
print(f"Medium:{Medium_num}")
print(f"Low:{Low_num}")
print(f"Total:{Total}")
print(f"AVERAGE:{The_average:.2f}")
print()
print(f"Best_customer:{Worst_cust}({lowest_score})")
print(f"Worst_customer:{Best_cust}({highest_score})")

while True:
    print()
    print()
    print("========== MENU ==========")
    print("1. Show All Customers")
    print("2. Search for a Customer")
    print("3. Exit")
    print("==========================")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("========== CUSTOMER RISK REPORT ==========")
        print()
        print("Name", "Score", "Risk")
        for name, score, risk in zip(customers, scores, risk_levels):
            print(name, score, risk)
        print()
        print("=============== SUMMARY ================")
        print()
        print("High Risk:  ", High_num)
        print("Medium Risk:", Medium_num)
        print("Low Risk:   ", Low_num)
        print("Average Score:", round(The_average, 2))
        print()
        print("Best Customer: ", lowest_score, "(" + str(lowest_score) + ")")
        print("Worst Customer:", highest_score, "(" + str(highest_score) + ")")

    elif choice == "2":
        search_name = input("Enter customer name: ")
        found = False
        for name, score, risk in zip(customers, scores, risk_levels):
            if name.lower() == search_name.lower():
                print("Name:", name)
                print("Score:", score)
                print("Risk:", risk)
                found = True
        if not found:
            print("Customer not found!")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
