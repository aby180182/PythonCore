# 2.  Напишіть програму, яка пропонує користувачу ввести свій вік,
# після чого виводить повідомлення про те чи вік є парним чи непарним числом.
# Необхідно передбачити можливість введення від’ємного числа,
# в цьому випадку згенерувати власну виняткову ситуацію.
# Головний код має викликати функцію, яка обробляє введену інформацію.

try:
    val = int(input('input your age: '))
    if val <= 0:
        raise Exception('Age must be positive!')

    if val % 2 == 0:
        print(val, ' odd')
    else:
        print(val, 'even')

except ValueError:
    print('Value Error!')
except Exception as e:
    print('Error!', e)
finally:
    print('Thank you!')


def enterage(age):
    if age < 0:
        raise ValueError("Only positive integers are allowed")

    if age % 2 == 0:
        print("age is even")
    else:
        print("age is odd")


try:
    num = int(input("Enter your age: "))
    enterage(num)

except ValueError as e:
    print("Only positive integers are allowed!!!", e)
except:
    print("something is wrong")