def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i += 1
    return res


def main():
    print(create_array(9))


if __name__ == '__main__':
    main()