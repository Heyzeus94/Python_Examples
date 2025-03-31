#Asking for the input
P = int(input("Enter number of packages purchased: "))

#Calculating total price
total_price = P * 99

#condition #1
if P >= 10 and P <= 19:
    d = total_price * 0.1
    final_price = total_price - d
    print(f"Discount Amount:${d:.2f}")
    print()
    print(f"Total Amount:${final_price:.2f}")
    print()
#Condition #2
elif P >= 20 and P <= 49:
    d = total_price * 0.2
    final_price = total_price - d
    print(f"Discount Amount:${d:.2f}")
    print()
    print(f"Total Amount:${final_price:.2f}")
    print()

#Condition #3
elif P >= 50 and P <= 99:
    d = total_price * 0.3
    final_price = total_price - d
    print(f"Discount Amount:${d:.2f}")
    print()
    print(f"Total Amount:${final_price:.2f}")
    print()
#Condition #4
elif P >= 100:
    d = total_price * 0.4
    final_price = total_price - d
    print(f"Discount Amount:${d:.2f}")
    print()
    print(f"Total Amount:${final_price:.2f}")
    print()
