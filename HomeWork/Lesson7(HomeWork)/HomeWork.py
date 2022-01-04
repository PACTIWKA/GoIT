children = {
   'Andri' : 3,
   'Lan' : 4,
   'Vlad' : 5,
   'Ana' : 2,
}
search_5 = [4,5]
new_list = dict() 
for key, value  in children.items():
    if value in search_5:
        new_list.update({key:value})
        print(new_list)
        

