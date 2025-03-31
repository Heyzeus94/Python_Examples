def string_total(string):
    total = 0
    for ch in string:
        ch=int(ch)
        total+=ch
    return total
def main():
    string = input('Enter a string of numbers: ')
    total=string_total(string)
    print('Sum of dingle digit numbers in the string:',total)
main()
