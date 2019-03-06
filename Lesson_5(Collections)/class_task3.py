# 3.  Написати програму, яка обчислює факторіал числа, яке користувач вводить.
# (не використовувати рекурсивного виклику функції)

fac = int(input('Enter number: '))
res = 1
for x in range(2, fac+1):
    res *= x
print('No negative numbers' if fac < 0 else 'Factorial of {} is {}'.format(fac, res))

