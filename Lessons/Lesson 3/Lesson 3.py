class_10a = ['Igor' , 'Vany' , 'leon'] #Class  
for pupils in class_10a:
    print(pupils)
else:
    print ('Всі учні')

Message = 'Hi Dima' #Message Dima
for char in Message:
    print(char , end=' ')

left = int(input('Left:'))
right = int(input('Right:'))

num = range(left , right) #Num for num range
sum = 0 

for q in num :
    sum += int(q)
    print(sum)
    

numbers = input().split()  #Split 

suma = 0 
for sum in numbers:
    suma += int(numbers)

print(suma)

fruit = ['Apple' , 'banana' , 'water']

need = 'banana'

for need_food in fruit:
    print(fruit)
    if need_food == need:
        print (need ,'in menu')
        break
else:
    print(need ,'not in menu')

