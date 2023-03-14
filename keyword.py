### Using the Or keyword to check value in list
names = ['tony','frank','mary','peter']
username = input("please enter your username you want to use\n")
if username in names:
    print('username already taken')
else:
    print('This username is avaliable')