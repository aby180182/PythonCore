# 4.  Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня,
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) .
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.



try:
    val = int(input('input number from 1 to 7: '))
    if 8 > val > 0:
        d = {
            1: 'Monday',
            2: 'Tuesday',
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday',
            6: 'Satarday',
            7: 'Sunday'
        }
        print(d[val])

    else:
        raise Exception('Number must be less than 8 and greater than 0')
except ValueError:
    print('Value Error!')
except Exception as e:
    print('Error!', e)
finally:
    print('Thank you!')
