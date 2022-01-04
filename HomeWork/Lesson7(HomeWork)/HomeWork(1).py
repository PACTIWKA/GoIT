wather = {
    'Киев' : 14,
    'Запорожье' : 17,
    'Херсон' : 18,
    'Львов' : 12  ,
    'Миколаїв' : 14
}
sum = 0
wether_2 = len(wather)
for sum_middle in wather.values():
    sum += sum_middle
    middle_wather = sum/wether_2
    print(f'Middle warp = {middle_wather}')
    
