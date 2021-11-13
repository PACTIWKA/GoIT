Good_1 = ['мило','паста','картопля','молоко']
Good_2 = ['чай','печиво','молоко','сир']
for i in Good_1:
    print ('search', i)
    for j in Good_2:
        if i == j:
            print('in 2 good')


while True:
    name = input('Enter name: ')
    if name == 'Vlad' :
        print('Hi brather')
        break
    else:
        print(name)
suma = 0 
a = 1 
while suma <= 100:   
    suma += a**2
    print(a)
    a = a + 1


min_number = 20
max_numaber = 130

while True:
     namber = int(input('Enter namber: '))

     if namber < min_number:
         continue
     if namber > max_numaber :
         print (namber)
         break
print('End') 


pupils = list()
print(pupils)

pupils = ['Kolya', 'Vlad', 'Ivan', 'Kata']
pupils = list(('Kolya', 'Vlad', 'Ivan', 'Kata'))

print(pupils)
pupil = pupils[2]
print(pupil)
pupils.append ('Kolya')
pupils.remove ('Vlad')
print(pupils)

best_pupil =pupils.pop(0)
print(best_pupil)
del pupils[2]
print(pupil)