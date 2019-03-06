#1 Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.

list_ = []
while True:
    num = int(input('Next number...'))
    list_.append(num)
    print('List: {}\nMax number: {}\nMin number: {}\n'.format(list_, max(list_), min(list_)))



#2 В інтервалі від 1 до 10 визначити числа
# •  парні, які діляться на 2,
# •  непарні, які діляться на 3,
# •  числа, які не діляться на 2 та 3

values1 = [x for x in range(1, 10) if x % 2 == 0]
print('even multiple 2: ', values1)
values2 = [x for x in range(1, 10) if x % 3 == 0]
print('even multiple 3: ', values2)
values3 = [x for x in range(1, 10) if x % 2 != 0 and x % 3 != 0]
print('even not divisible 2 and 3: ', values3)



# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.
# (не використовувати рекурсивного виклику функції)

fac = int(input('Enter number: '))
res = 1
for x in range(2, fac+1):
    res *= x
print('No negative numbers' if fac < 0 else 'Factorial of {} is {}'.format(fac, res))



# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач.
# Якщо логін вірний (First), то привітайте користувача.
# Якщо ні, то виведіть повідомлення про помилку.
# (використайте цикл while)

login = input('Login: ')
while login != 'First':
    login = input('Login: ')
    print('Hi!' if login=='First' else 'Error!' )



# 5.  Перший випадок.
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число.
#  При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).
while True:
    num = int(input('Input next number: '))
    if num > 0:
        print(num)
    else:
        print('break')
        break



# 6.  Другий випадок.
# На початку на вхід подається кількість елементів послідовності, а потім самі елементи.
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

amount_of_numbers = int(input('Input amount of numbers: '))
list_of_numbers = []
for x in range(amount_of_numbers):
    i = int(input('Input the next number: '))
    if i > 0:
        list_of_numbers.append(i)
    else:
        print(list_of_numbers, 'break')
        break
    print(list_of_numbers)



# 7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел
# (наприклад 10 equals 2 * 5
#                     11 is a prime number
#                     12 equals 2 * 6
#                     13 is a prime number
#                     14 equals 2 * 7
#                      ………………….)


# for x in range (10, 31):
#     print(x, 'is a prime number' if x % 2 != 0 else 'equals 2 * ',int(x/2))


[(print(x, 'is a prime number' if x % 2 != 0 else 'equals 2 * {0:.0f} '.format(x/2))) for x in range (10, 31)]




# 8.  Відсортувати слова в реченні в порядку їх довжини

string = 'Sed dapibus, felis ut aliquam pharetra, tortor sapien vestibulum neque, vel sodales tortor sem quis tortor.'
print(string)
string = string.split()
string.sort(key=len)
# string.reverse()
string = ' '.join(string)
print(string)

