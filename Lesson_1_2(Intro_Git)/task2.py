def calculate_two_numbers():
    a = float(input('Input a: '))
    b = float(input('Input b: '))
    print('a =', a)
    print('b =', b)
    print('a + b =', a + b)
    print('a - b =', a - b)
    print('a * b =', a * b)
    try:
        print('% modulus =', a % b)
    except:
        print('No zero division')
    print('** exponent =', a ** b)
    try:
        print('a / b =', a / b)
    except:
        print('No zero division')




def main():
    calculate_two_numbers()


if __name__ == '__main__':
    main()