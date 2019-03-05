def prod_num():
    num = input('Input 4-digit number: ')
    prod = int(num[0]) * int(num[1]) * int(num[2]) * int(num[3])
    print(prod)
    print(num[::-1])
    print(''.join(sorted(num)))


def main():
    prod_num()


if __name__ == '__main__':
    main()