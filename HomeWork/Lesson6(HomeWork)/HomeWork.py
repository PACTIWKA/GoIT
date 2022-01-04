Message = 'В мене е два яблука підрахуй скільки було раніше?'
split = Message.split() 

large_worb = max(split, key=len)

print('Cамое длиное слово:',large_worb) 