first = int(input('Первое чило: '))
second = int(input('Второе число: '))
num = range(first , second)
sum = 0
for number in num:
    sum += int(number)**2
    print (sum)