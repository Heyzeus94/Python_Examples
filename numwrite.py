from random import randint

def generate_number():
    return randint(1,500)
def write_to_file(count):
    with open("random numbers.txt","w") as file:
        for i in range(count):
            num = str(generate_number())
            file.write(num+ "\n")
        file.close()

if __name__ == "__main__":
    count = int(input("Enter number of random numbers to generate: "))
    write_to_file(count)
    print("Written %d random numbers to file \"random numbers.txt\"." %count)
