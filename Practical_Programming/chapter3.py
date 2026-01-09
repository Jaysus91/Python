# Designing and using functions
day_temp = 3
night_temp = 10

difference = abs(day_temp-night_temp)
print(difference)

# Functions can be called inside functions
print(pow(abs(-2),round(4.3)))

def convert_to_celcius(fahrenheit: float):
    x=round((fahrenheit - 32) * 5/9,2)
    return print(x)

convert_to_celcius(212)

# Function I made for finding if a number is even or odd
def even_or_odd(number: int) -> str:
    """Given an integer, returns if that number is even or odd"""
    x = number % 2
    if x == 1:
        print("odd")
    if x == 0:
        print("even")
    else: 
        print("Number must be an integer")

even_or_odd(6)

# Days difference function
def days_difference(day1: int, day2: int):
    return day2-day1

def get_weekday(current_weekday: int, day_ahead: int):
    """Returns which day of the week it will be 'days_ahead' from 'current_weekday'
    
    days_ahead is the number of days after today."""
    return (current_weekday + day_ahead -1) % 7 + 1

weekdays = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
def get_birthday_weekday(current_weekday: int, current_day: int, birthday_day: int):
    """Returns the day of the week it'll be on birthday_day,
    given that the day of the week is current_weekday and the
    day of the year is current_day."""
    days_diff=days_difference(current_day, birthday_day)
    x= get_weekday(current_weekday, days_diff)
    return weekdays[x]

print(get_birthday_weekday(5,3,360))
