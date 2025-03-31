# This will define function to get the seating price based on category

def getSeatingPrice(category):
    if category == 'A':
        return 20.0
    elif category == 'B':
        return 15.0
    elif category == 'C':
        return 10.0
    else:
        return 0.0 #for invalid category



def getUserInput():
    category = input('Enter the category (A, B or C):')
    num_tickets = int(input('Enter the number of tickets required: '))
    return category, num_tickets

def showIncome(income_Aseats, income_Bseats, income_Cseats):
    print(f"Income from class A seats: ${income_Aseats:.2f}")
    print(f"Income from class B seats: ${income_Bseats:.2f}")
    print(f"Income from class C seats: ${income_Cseats:.2f}")
    total_income = income_Aseats + income_Bseats + income_Cseats
    print(f"Total income: ${total_income:.2f}")


def main():
    income_Aseats = 0.0
    income_Bseats = 0.0
    income_Cseats = 0.0

    need_more_tickets = 'Y'

    while need_more_tickets == 'Y':
        category, num_tickets = getUserInput()
        seating_price = getSeatingPrice(category)
        income = seating_price * num_tickets

        if category == 'A':
            income_Aseats += income
        elif category == 'B':
            income_Bseats += income
        elif category == 'C':
            income_Cseats += income

        need_more_tickets = input('Do you need more tickets? Press Y to continue or press N to quit: ')

    showIncome(income_Aseats, income_Bseats, income_Cseats)


# Call to main function
if __name__ == '__main__':
    print('Welcome to the Stadium Seating Application')
    print('Category A - $20')
    print('Category B - $15')
    print('Category C - $10')
    main()
        
