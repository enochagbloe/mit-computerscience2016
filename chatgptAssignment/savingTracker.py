#Simple saving tracker

monthly_salary = int(input("Enter your monthly salary: "))
portion_saved = float(input("Enter the percentage of your salary in decimals: "))
saving_goals = int(input("Enter your saving goal: "))

#3percent intrest on every monthly_salary
monthly_intrest_rate = 0.03 / 12

#det months
months= 0

#set current savings
current_savings = 0

while current_savings < saving_goals:
    monthly_saving = current_savings * monthly_intrest_rate
    current_savings += monthly_salary * portion_saved
    current_savings += monthly_saving
    months += 1
print(f" number of months: {months}")
print(f"Total savings: {current_savings}")