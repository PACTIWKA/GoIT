products = ['апесин','мадарин','лемон']
products_sold = list()

while True:
    product = input("Введить продукт а щоб закінчити 0: ")
    
    if product == '0':
        break
    else: 
        products.append(product)

print(products)

