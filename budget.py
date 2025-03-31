def main():
    budget = float(input("Enter your budget for the month: "))
    total_spent = 0.0

    while True:
        expense = float(input("Enter an expense amount (0 to stop): "))
        if expense == 0:
            break
        total_spent += expense

    print(f"Budgeted: ${budget:,.2f}")
    print(f"Spent: ${total_spent:,.2f}")

    if budget > total_spent:
        print("WELL DONE!")
    elif budget < total_spent:
        print("PLAN BETTER NEXT TIME!")
    else:
        print("GOOD PLANNING!")

if __name__ == '__main__':
    main()
