#salary growth saving simuation
#salary increased by 7% every year
#key things to note
#25% downpayment of the dreamhome
#every year ur portion saved increases by 4%

annual_salary = int(input("Enter your annual salary: "))
#note that the portion saved is in percentage of the monthly savings
portion_saved = float(input("Enter the percentage of your salary to save, as decimal: "))
dream_home = int(input("Enter your dream Home amount: "))

#set your current savings to zero
current_savings = 0

#months
months = 0

# the accual monthly salary
monthly_salary = annual_salary / 12

#the intrest for the savings in the bank
saving_intrest = 0.04 / 12

#downpayment of the house
down_payment = dream_home * 0.25

# run the loop
while current_savings < down_payment:
    #get the monthly intrest on the savings
    monthly_interest = current_savings * saving_intrest
    current_savings += monthly_salary * portion_saved
    current_savings += monthly_interest
    months+=1
print(f"Number of months: {months}")