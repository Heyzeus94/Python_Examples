def is_prime(n) :
    count = 0 # counter variable
    for i in range(1, n + 1): #loop from 1 until n
        if n % i == 0 :
            count += 1
    if count == 2:
        return True
    else:
        return False

def main():
    n = 10
    print('number is prime')
    print('------------------')
    for i in range(1, n + 1):
        if is_prime (i):
            print(str(i) + ' prime')
        else:
                print(str(i) + ' not prime')


main()
