###Other ways to loop dictionary 
birthday_months = {
    'tony' : 'november',
    'pat' : 'june',
    'mary' : 'may',
}
for name in birthday_months.keys():
    print(name.title())
for months in birthday_months.values():
    print(months.title())

for months in set(birthday_months.values()):
    print(months.title())