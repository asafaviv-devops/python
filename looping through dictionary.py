### looping trough dictionary
birthday_months = {
    'tony' : 'november',
    'pat' : 'june',
    'mary' : 'may',
}
for key,value in birthday_months.items():
    print('\nname: ' + key)
    print('birthday_month: ' + value)
    
print(birthday_months)
book_1 = {
    'name' : 'elon musk',
    'author' : 'ashlee vance',
    'price' : '14.99' ,
    'publisher' : 'virgin books',
}
for key, value in book_1.items():
    print("\nKey: " + key)
    print("value " + value)