def main():
    #Declaring Variables
    
    customer_type = input("Enter 'n' for new customer or 'e' for existing customer: ")
    invest = float(input("Please enter the initial investment amount: "))

    #Define interest rates
    if customer_type == 'n':
        interest_rate = 3.25
    elif customer_type == 'e':
        if invest < 1000:
            interest_rate = 3.0
        else:
            interest_rate = 3.5

    else:
        print("Invalid customer type. Please enter 'n' for new or 'e' for existing.")
        return

    #Calculate the ending balance
    end_balance = invest * (1 + interest_rate / 100)

    print(f"Interest rate = {interest_rate}%")
    print(f"Ending balance: ${end_balance:.2f}")

if __name__ == "__main__":
    main()
