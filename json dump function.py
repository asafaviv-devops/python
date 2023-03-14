### Working with json.dump () function
import json
phone_numbers = [123456789]
filename = 'Desktop\python\phone_number.json'
with open(filename, 'w') as file_object:
    json.dump(phone_numbers, file_object)