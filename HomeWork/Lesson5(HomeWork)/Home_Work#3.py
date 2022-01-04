Numbers = [
    '+380997685996',
    '+34434578',
    '3982602009',
    '+3804413759',
    '+3809834845',
    '9670599468295',
    '+73249589204'
]

Index = '+38'
Operators = ['067', '068', '097', '044', '050', '099', '066', '073', '093', '063']

for number in Numbers:
    if len(number) < 13 and number[:3] != Index and number[3:6] not in Operators:
        print(number)