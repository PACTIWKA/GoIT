Trevel = ['Николаев','Турция','Крым']
Next_Trevel = input('Место:')
for Treverling in Trevel:
    print (Trevel)
    if Trevel == Next_Trevel:
        print(Next_Trevel,'поїздка не перший раз')
        break
else:
    print(Next_Trevel,'перший раз')