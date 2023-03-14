### using the try-except block
from asyncio import exceptions
from traceback import print_exc
import traceback
try:
    print(5/0)

except ZeroDivisionError:
    print('you cannot divide by Zero')
    
print('Please enter another number')
