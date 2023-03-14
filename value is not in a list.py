### checking if value is not in a list
admin_users = ['tony','frank']
username = input('please enter your username\n')
if username not in admin_users:
    print('you don\'t have access')
else:
    print('access granted')
