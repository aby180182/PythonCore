def who_a_u():
    name = input('What is your name: ')
    age = input('How old are you?: ')
    location = input('Where do you live?: ')
    print("Hello, {}.\nYour age is {}.\nYou live in {}\n".format(name, age, location))


def main():
    who_a_u()


if __name__=='__main__':
    main()