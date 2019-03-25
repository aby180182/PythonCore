# 1.  Напишіть програму,
# яка пропонує користувачу ввести ціле число
# і визначає чи це число парне чи непарне, чи введені дані коректні.


try:
    val = int(input('input number: '))
    if val % 2 == 0:
        print(val, ' odd')
    else:
        print(val, 'even')
except ValueError:
    print('Value Error!')
except:
    print('Error!')
finally:
    print('Thank you!')

# n = input("Input entire number: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("\n You entered incorrect data!\n")
#         n = input("Input entire number:\n ")
#
# if n % 2 == 0:
#     print("{0} is the even number.".format(n))
# else:
#     print("{0} is the odd number.".format(n))
