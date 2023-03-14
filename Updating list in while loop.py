## Updating list in while loop
unconfirmed_users = {'tony','frank','mary'}
confirmed_users = []
while unconfirmed_users:
    current_user =unconfirmed_users.pop()
    print("Verifying user:" + current_user.title())
    confirmed_users.append(current_user)
print ("The following users have been confirmed")
for confirm_user in confirmed_users:
    print(confirm_user.title())
