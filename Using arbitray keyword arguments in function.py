### Using arbitray keyword arguments

def seat_profile(first, last, **passenger_info):
    profile= {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in passenger_info.items():
        profile[key] = value
    return profile
passenger_profile = seat_profile('asaf', 'aviv', seat_num=36, breakfast_order='yes')
print(passenger_profile) 