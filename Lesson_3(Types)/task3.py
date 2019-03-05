def change_vars(a, b):
    print('a = ', a, 'b = ', b)
    a, b = b, a
    print('a = ', a, 'b = ', b)


def main():
    change_vars(a=100, b=-100)


if __name__ == '__main__':
    main()



