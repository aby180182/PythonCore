# 8.  Відсортувати слова в реченні в порядку їх довжини 

string = 'Sed dapibus, felis ut aliquam pharetra, tortor sapien vestibulum neque, vel sodales tortor sem quis tortor.'
print(string)
string = string.split()
string.sort(key=len)
# string.reverse()
string = ' '.join(string)
print(string)

