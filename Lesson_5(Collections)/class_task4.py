# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач. 
# Якщо логін вірний (First), то привітайте користувача. 
# Якщо ні, то виведіть повідомлення про помилку. 
# (використайте цикл while)

login = input('Login: ')
while login != 'First':
    login = input('Login: ')
    print('Hi!' if login=='First' else 'Error!' )
