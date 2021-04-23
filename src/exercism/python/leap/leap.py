def leap_year(year):
    try:
        return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
        
    except ValueError as err:
        raise Exception("Incorrect number inserted, please try again\n Error:", err)
