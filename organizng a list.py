### organizing a list
# creating a list of months
from calendar import WEDNESDAY


birthday_months = ['may','november','june']
birthday_months.sort()
print(birthday_months)
# using reverse sort method
birthday_months = ['may','november','june']
birthday_months.sort(reverse=True)
print(birthday_months)
birthday_months = ['may','november','june']
print(sorted(birthday_months))
print(birthday_months)
birthday_days = ['monday','thuesday','wednesday','friday']
birthday_days.reverse()
print(birthday_days)