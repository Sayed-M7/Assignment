The_team_members=int(input("what is the number of the team member:"))
Months_number=float(input("the number of months?:"))
Monthly_salary=float(input("what is the monthly salary a member:"))
Total_cloud_coast=float(input("what is the total cloud coast for the whole project"))

salary_coast= The_team_members*Months_number*Monthly_salary
subtotal=salary_coast+Total_cloud_coast
vat=subtotal*0.14
TOTAL=subtotal+vat

print(f"salary coast: {salary_coast:,.2f}, cloud coast: {Total_cloud_coast:,.2f}, subtotal:{subtotal:,.2f}, vat:{vat:,.2f}, TOTAL:{TOTAL:,.2f}" )