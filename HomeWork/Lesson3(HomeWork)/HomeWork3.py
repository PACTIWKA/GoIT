Trevel = ['Николаев','Турция','Крым']
Next_Trevel = input('Место:')
for Treveling in Trevel:
    print (Trevel)
    if Treveling == Next_Trevel:
        print(Next_Trevel,'поїздка не перший раз')
        break
else:
    print(Next_Trevel,'перший раз')