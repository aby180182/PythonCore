def fib(n):
    fib_list = [0, 1]
    n1 = 0
    n2 = 1
    for i in range(2, n):
        n1, n2 = n2, n1 + n2
        fib_list.append(n2)
    return(fib_list)





def main():
    print(fib(10))


if __name__ == '__main__':
    main()
