def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def factorial2(n):
    res = 1
    for x in range(2, n+1):
        res *= x
    return res


def main():
    print(factorial2(10))


if __name__ == '__main__':
    main()
