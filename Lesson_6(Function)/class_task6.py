# 6.  Написати програму калькулятор, яка складається з наступних функцій:

# головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії,
# калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора,
#  після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

sum = lambda a, b: a + b
difference = lambda a, b: a - b
product = lambda a, b: a * b
division = lambda a, b: a / b

def main():
    while True:
        a = float(input("First number: \n"))
        b = float(input("Second number: \n"))
        choise = input("Do your choise:\n1 - sum\n2 - difference\n3 - product\n4 - division\n0 - exit\n")
        if choise == '1':
            print(sum(a, b))
        elif choise == '2':
            print(difference(a, b))
        elif choise == '3':
            print(product(a, b))
        elif choise == '4':
            print(division(a, b))
        elif choise == '0':
            print("Thank you for choosing our software\n")
            break
        else: continue

if __name__ == "__main__":
    main()