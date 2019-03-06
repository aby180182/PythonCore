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