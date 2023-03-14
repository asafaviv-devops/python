### using the input statment
from turtle import title


welcome = input("Welcome, What's your name? ")
print("Hello " + welcome.title())
welcome = input("what is your role? ")
if welcome == "linux":
    print('i want devops')
else: print("I want linux")