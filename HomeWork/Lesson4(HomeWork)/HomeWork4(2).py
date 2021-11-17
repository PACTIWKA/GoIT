Telephone = [
 ['Phone' ,'Honor', 12100],
 ['NoteBook' , 'Lenovo' , 10000],
 ['NoteBook', 'Hp' , 12500],
 ['Phone' , 'Samsung', 12300]
]

for shop in Telephone:
    j = input('Введите что иммено?(Phone|NoteBook): ')
    if j == 'Phone': 
        print  (Telephone[0]) 
        print  (Telephone[3])
        break
    elif j == 'NoteBook':
        print (Telephone[1]) 
        print  (Telephone[2])
        break
for sum in shop:
    c = int(input('Введите цену(макс): '))
    if c <= shop[2]:
        print (shop)