#1 Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.


list_ = []
while True:
    num = int(input('Next number...'))
    list_.append(num)
    print('List: {}\nMax number: {}\nMin number: {}\n'.format(list_, max(list_), min(list_)))

