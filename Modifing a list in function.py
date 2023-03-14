# Modifiying a list in function


def passangers(not_checked_in1, checked_in1):

    while not_checked_in:
        current_passenger = not_checked_in1.pop()
        print("checking in passenger:" + current_passenger)
        checked_in1.append(current_passenger)




def show_checked_in_passangers(checked_in1):
    print("\nThe following passenger have been checked_in")
    for passangers1 in checked_in1:
        print(passangers1)


if __name__ == '__main__':
    not_checked_in = ['Elinor', 'Aviv', 'Yossi', 'Avi']
    checked_in = []

    passangers(not_checked_in, checked_in)
    show_checked_in_passangers(checked_in)

