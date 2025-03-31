def display_larger_than_n_list(n, number_list):
    larger_numbers = [x for x in number_list if x > n]

    print(larger_numbers)
    larger_numbers.sort()

    with open('sortedNumbers.txt', 'w') as outfile:
        for num in larger_numbers:
            outfile.write(str(num) + '\n')

def main():
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print('Number:', number)
    print('List of numbers:\n', number_list, sep ='')
    print('List of numbers that are larger than ', number, ':', sep='')

    display_larger_than_n_list(number, number_list)
if __name__ == '__main__':
    main()
