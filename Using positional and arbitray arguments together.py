def assign_seats(seat, *requests):
    print("\nAssign seat " + str(seat) + " The following requests")
    for request in requests:
        print(request)


assign_seats(36, 'windows seat')

