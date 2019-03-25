# 3.  Напишіть програму для обчислення частки двох чисел,
# які вводяться користувачем послідовно через кому,
# передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій.
# Використати блоки else та finaly.
try:
    num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")
except ValueError:
    print("Value Error.")
except SyntaxError:
    print("Comma is missing. Enter numbers numbers separated by comma like this 1, 2")
# 65866hgjh75785
except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")


try:
    a, b = map(int, input("Enter four numbers separated by comma\n").split(','))
    div = a / b
    print(div, '\n')
except SyntaxError:
    print('Syntax Error!')
except ValueError:
    print('Value Error!')
except ZeroDivisionError:
    print('ZeroDivisionError!')
except Exception:
    print('Error!')
else:
    print('No exception')
finally:
    print('Thank you!')
