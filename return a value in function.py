### returning a value in function
def format_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

teacher = format_name('asaf','aviv')
print(teacher)

def username_email (email_address):
    username = email_address.title()
    return username
user = username_email('asaf.aviv21@gmail.com')
print(user)