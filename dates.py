month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
year = int(input("Enter the year: "))

if(month < 1 or month > 12):
    print("Error - Month is invalid")
    exit()
if(day < 1 or day > 31):
    print("Error - Day is invalid")
    exit()
if(year < 0 or year > 99):
    print("Error - Year is invalid")
    exit()
# Display Output
print("The date is ",month,'/',day,'/',year)

if(month*day == year):
      print("This is a magic date.")
else:
    print("This is not a magic date.")
