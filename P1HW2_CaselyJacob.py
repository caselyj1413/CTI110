# This program calculats and displays travel expenses
 
 # 2-16-2023

 # CTI-110 P1HW2 - Travel Expense

 # Jacob Casely

print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter budget: "))
print()
name = input("Enter your travel destination: ")
print()
gas = float(input("Enter the amount you think you will spend on gas: "))
print()
accom = float(input("Enter the amount you think you will spend on accommodations: "))
print()
food = float(input("Enter the amount you think you will spend on food: "))
print()
print("-"*12,"Travel Expenses",12*"-")
print("Location: ", name)
print("Initial Budget:", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", accom)
print()
balance = budget - gas - accom - food
print("Remaining Balance: ", format(balance,',.0f'))

