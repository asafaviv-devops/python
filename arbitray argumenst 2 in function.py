### Arbitray arguments
def create_passenger(*requests):
    print("\nTHe passenger has requested ")
    for request in requests:
        print(request)


create_passenger('windows seat', 'seat near the top of the plane', 'pre-order a breakfast' )


    