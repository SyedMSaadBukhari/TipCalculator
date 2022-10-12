print("Welcome to the tip calculator. ")
Bill = float(input("What was the total bill? $"))
Tip_Percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
No_of_People = float(input("How many people to split the bill? "))


Total_Bill = round(Bill + Bill * (Tip_Percentage / float(100)), 2)
Each_person_pay = round((Total_Bill / No_of_People), 2)
Each_person_pay = "{:.2f}".format(Each_person_pay)
print(f"Each person should pay: ${Each_person_pay}")

