continents = [ 'Америка Північна','Америка Південна','Антарктида']
while True:
    continent = input('Введите названия которые хотите добавть чтобы закончить !')
    if continent == '!':
        break
    else:
        continents.append(continent)



continents.sort(reverse=True)
print(continents)