def leap_year(year):
    leap = False
    if (year % 4 == 0):
        leap = True
    elif (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        leap = False
    # elif (year % 100 == 0) and (year % 400 == 0):
        # leap = True

    return leap


print(leap_year(2000))