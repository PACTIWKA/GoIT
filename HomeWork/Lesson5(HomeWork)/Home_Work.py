Name = 'Vladislav'
Name_seen = []

for i in Name :
    if i not in Name_seen:
        print( i, '-',Name.count(i))
        Name_seen.append(i)