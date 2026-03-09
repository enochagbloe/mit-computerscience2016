# totalcost
# portion_down_payment = 0.25
# current_savings



annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as decimal: "))
dream_home = int(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

down_payment = 0.25 * dream_home
current_savings = 0
r = 0.04
months = 0
semi_annual_raise_months = 6
semi_annual_raise_count = 0

monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved 

#loop to calculate the number of months needed to save for the down payment
while current_savings < down_payment:
    monthlty_interest = current_savings * r / 12
    current_savings +=  monthlty_interest
    current_savings += monthly_savings
    months += 1
    semi_annual_raise_count += 1
    if semi_annual_raise_count == semi_annual_raise_months:
        monthly_salary += monthly_salary * semi_annual_raise
        monthly_savings = monthly_salary * portion_saved
        semi_annual_raise_count = 0
print("Number of months: " + str(months))
