### Using if statement with lists
from asyncio import shield


shoping_cart = ['pens','paper','stapler','post-its']
for item in shoping_cart:
    if item == 'pens':
        print('This ' + item + ' is out of stock')
    else:
        print('Adding '+ item + 'to your order.') 
    
print('your order is complete')

shoping_cart = []
if shoping_cart:
    for item in shoping_cart:
        print('Adding ' + item + ' to your order.')
else:
    print("please adding items to your shoping_cart")
shoping_cart_len = len(shoping_cart)
print(shoping_cart_len)
if shoping_cart_len > 0:
    print('Adding ' + str(shoping_cart) + 'items.')
else:
    print('please adding items to your cart')