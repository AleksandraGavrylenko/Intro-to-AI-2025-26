item = input('item name ')
quantity = int(input('amount of item '))
price = float(input('price of item '))

if quantity>0:
    if price>0:
        print(f'Item: {item}, quantity: {quantity}, price: ${price}, total: ${quantity*price}')