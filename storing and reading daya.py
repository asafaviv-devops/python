### storing and reading user data
import json
username = input('What is your username? ')

filename = 'username.json'
with open(filename,'w') as file_object:
    json.dump(username, file_object)
    print("Thank you , I wil remember you when you come back")