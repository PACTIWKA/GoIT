Line = input('Введите строку: ')
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
New_line = ''

for i in Line:
    if i not in Numbers:
        New_line += i
print(New_line)