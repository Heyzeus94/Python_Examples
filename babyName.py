
def main():
    with open("BoyNames.txt", "r") as file:
        popular_boys = [line.rstrip() for line in file]

    with open("GirlNames.txt", "r") as file:
        popular_girls = [line.rstrip() for line in file]

    boy = input("Enter a boy's name, or N if you do not wish to enter a boy's name: ")
    girl = input("Enter a girl's name, or N if you do not wish to enter a girl's name: ")

    if boy == "N":
        print("You chose not to enter a boy's name.")
    elif boy in popular_boys:
        print(f"{boy} is one of the most popular boy's names.")
    else:
        print(f"{boy} is not one of the most poular boy's names. ")

    if girl == "N":
        print("You chose not to enter a girl's name.")
    elif girl in popular_girls:
        print(f"{girl} is one of the most popular girl's names.")
    else:
        print(f"{girl} is not one of the most popular girl's names.")

if __name__ == "__main__":
    main()
    
