### using dictionary in  a list
stock_items = []

for blue_pen in range(0,50):
    new_blue_pen = {
        'color' : 'blue',
        'type' : 'ballpoint',
        'price' : '1.99',
    }
    stock_items.append(new_blue_pen)
print(stock_items)
for blue_pen in stock_items[0:5]:
    if blue_pen['price'] == '1.99':
        blue_pen['price'] = '0.53'
print(stock_items[0:5])
    
