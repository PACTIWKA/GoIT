telephone = [
 ['phone' ,'Honor', 12100],
 ['notebook' , 'Lenovo' , 10000],
 ['notebook', 'Hp' , 12500],
 ['phone' , 'Samsung', 12300]
]

j = input('Введите что иммено?(Phone|NoteBook): ')
for type in telephone:
  if j in type:
    print(type)
c = int(input('Введите цену: '))
for type in telephone:
  if type[2] < c :
    print(type)