# x < 6
# 6 < x <= 8
# 8 < x <= 14
# x > 14

while True:
    try:
        x = int(input("Enter number: \n"))
        val = {x < 6: 'x < 6', 6 <= x < 8: '6 < x < 8', 8 <= x < 14: '8 < x < 14', x >= 14: 'x > 14'}[True]
        print(val)
    except ValueError:
        print('ValueError')







    # val = {x < 6: 'x < 6', 6 <= x < 8: '6 < x < 8', 8 <= x < 14: '8 < x < 14', x >= 14: 'x > 14'}.get(True, 'Value Error!')
    # print(val)



    # val2 = 'x < 6' if x < 6 else '6 < x < 8' if 6 <=x< 8 else 'x > 14'
    # print(val2)

