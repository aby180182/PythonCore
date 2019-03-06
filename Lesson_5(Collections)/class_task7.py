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
