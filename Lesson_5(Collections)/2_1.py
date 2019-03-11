def longest(s1, s2):
    l = list(s1) + list(s2)
    print(l)
    for i in l:
        print(i)
        print(l.count(i))
        if l.count(i) > 1:
            l.pop()

            print(l)
    print(l)
    print('sss', l.count('a'))
    print(''.join(sorted(l)))

    return ''.join(sorted(l))


def main():
    print(longest('qaaaa', 'qwertygfd'))

if __name__ == '__main__':
    main()