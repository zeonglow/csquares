from itertools import zip_longest
from math import fabs

def global_quadrant(latitude: float, longitude: float):
    if latitude >= 0 and longitude >= 0:
        return '1'
    elif latitude < 0 and longitude < 0:
        return '5'
    elif latitude < 0 and longitude >= 0:
        return '3'
    elif latitude >= 0 and longitude < 0:
        return '7'

def other_cycle(latitude, longitude):
    if latitude < 5 and longitude < 5:
        code = '1'
    elif latitude < 5 and longitude >= 5:
        code = '2'
    elif latitude >= 5 and longitude < 5:
        code = '3'
    elif latitude >= 5 and longitude >= 5:
        code = '4'
    return code + str(latitude) + str(longitude)

def range_valid(latitude: float, longitude: float):
    if latitude >= -90 and latitude <= 90 and longitude >= -180 and longitude <= 180:
        return True
    return False

def prepare_code(code, is_latitude):
    if is_latitude:
        length = 2
        knock_back = 90.0
    else:
        length = 3
        knock_back = 180.0

    abs_code = fabs(code)

    if abs_code >= knock_back:
        abs_code = abs_code - 1

    parts = str(abs_code).split('.')
    zpad = len(parts[0])
    output = list(parts[0])

    while zpad < length:
        output.insert(0, '0')
        zpad = zpad + 1

    if len(parts) > 1 and parts[1] != '0':
        output.extend(parts[1])
    return output

def to_csquare(latitude, longitude):
    if not range_valid(latitude, longitude):
        raise ValueError('Invalid coordinates')

    csquare = [global_quadrant(latitude, longitude)]

    latitude_code = prepare_code(latitude, is_latitude=True)
    longitude_code = prepare_code(longitude, is_latitude=False)

    csquare.append(latitude_code.pop(0))
    csquare.append(longitude_code.pop(0))
    csquare.append(longitude_code.pop(0))

    for lat_digit, long_digit in zip_longest(
            latitude_code,
            longitude_code,
            fillvalue='0'):
        csquare.append(':')
        csquare.append(other_cycle(int(lat_digit), int(long_digit)))

    return ''.join(csquare)
