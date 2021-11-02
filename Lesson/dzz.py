Name = input('Name:')
ball = int(input('Ball:'))

if ball > 100:
    print ('Невозможный бал')
elif ball < 60:
    result  = "Не задовільно"
elif 60 <= ball <= 74:
    result = "Задовільно"
elif 75 <= ball <= 94:
    result = "Добре"
else: 
    result = "Відмінно"

print (Name,' flod: ',result)  