def readRandomNumbers():
    numbers = list()
    with open ("random numbers.txt", "r") as file:
        for line in file:
            numbers.append(int(line.rstrip()))
        file.close()
    return numbers
def displayData (numbers):
    print("The total of the numbers: %d" %sum(numbers))
    print("The number of random numbers read form the file : %d" %len(numbers))

if __name__ == "__main__":
    randomNumbers = readRandomNumbers()
    displayData(randomNumbers)
