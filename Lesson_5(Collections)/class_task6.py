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