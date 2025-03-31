amount = float(input("Enter the amount in dollars and cents (example: 10.63)"))

# Amount of pennies

total_pennies = int(amount * 100)

# Dollars
dollars = total_pennies // 100
remaining_pennies = total_pennies % 100

# Quarters
quarters = remaining_pennies // 25
remaining_pennies %= 25

#Dimes
dimes = remaining_pennies // 10
remaining_pennies %= 10

#Nickels
nickels = remaining_pennies // 5
remaining_pennies %= 5

#Leftover are remaining pennies

#Display output
print(f"Your amount {amount:.2f} consists of")
print(f"{dollars} dollars")
print(f"{quarters} quarters")
print(f"{dimes} dimes")
print(f"{nickels} nickels")
print(f"{remaining_pennies} pennies")
