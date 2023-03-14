### working with multiple list
in_stock = ['blue','pens','paper','staples']
shoping_cart = ['blue','pens','paper','staples','orange post-its']
for item in shoping_cart:
    if item in in_stock:
        print('Adding ' + item + 'to your order.')
    else:
        print('Sorry {} is not in stock.'.format(item))
print('Your order is complete.')
