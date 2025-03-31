def main():
    word_count = {}

    file_name = input('Enter the name of the input file: ')

    with open(file_name, 'r') as f:
        words = f.read().split()

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    print('word occurences')
    print('------------------------------------')
    while len(word_count) > 0:
        word, count = word_count.popitem()
        print(f'{word} {count}')

if __name__ == '__main__':
    main()
    
