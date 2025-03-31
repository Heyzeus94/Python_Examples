def main():
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    whitespace_count = 0

    with open('text.txt', 'r') as file:
        for char in file.read():
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
            elif char.isdigit():
                digit_count += 1
            elif char.isspace():
                whitespace_count += 1

    print(f'Uppercase letters: {uppercase_count}')
    print(f'Lowercase letters: {lowercase_count}')
    print(f'Digits: {digit_count}')
    print(f'Spaces: {whitespace_count}')

if __name__ == '__main__':
    main()
