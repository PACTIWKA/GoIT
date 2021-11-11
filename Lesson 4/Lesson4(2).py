products = ['апесин','мадарин','лемон']
products_sold = list()

while True:
    product = input("Введить продукт а щоб закінчити 0: ")
    
    if product == 0:
        break
    else: 
        product.append(product)

product.exstend(['Картопля','Пиво'])       
    
for product in products :
    print(product, end='')

product = input('Введить назву продукту(buy): ')
if product in products:
     product.remove(product)
     products_sold.append(product)
     print('Thx for buy')
else:
        print('Havent product')

print('')
product_index = int(input('sell product: '))

if 0 <= product_index < len(product):
    product = products.pop(product_index)

    products_sold.append(product)
    print('U buy', product)
    print('Thx')
else:
    print('Havent')

