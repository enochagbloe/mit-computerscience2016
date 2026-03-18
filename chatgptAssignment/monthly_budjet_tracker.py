monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
portion_saved = float(input("Enter the percentage of your income you want to save (in decimals): "))
saving_goal = int(input("Enter your saving goal: "))

month = 0

current_savings = 0

acutual_saving = (monthly_income - monthly_expenses) * portion_saved

potion_increase = portion_saved * 0.05
saving_goal_half = saving_goal / 0.5

while current_savings < saving_goal:
    current_savings += acutual_saving
    current_savings += current_savings * 0.02 / 12
    month += 1

    if current_savings >= saving_goal_half:
        portion_saved += potion_increase

print(f"It will take {month} months to reach your saving goal.")
print(f"Total savings: {current_savings:.2f}")
print(f"Final portion saved: {portion_saved:.2f}")