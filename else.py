### if-elif-else checker
balance = input("What is your balance\n")
if int(balance) <=50:
    print('You do not qualify for interest')
elif int(balance) < 100:
    print("your interest rate is 1%.")
else:
    print("your interest rate is 2%.")