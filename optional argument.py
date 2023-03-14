### Making argument optional
import re


def formatted_name(first_name,last_name,middle_name =''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

teacher = formatted_name('asaf','aviv','siman tov'.title())
print(teacher)
teacher = formatted_name('asaf','aviv'.title())
print(teacher)