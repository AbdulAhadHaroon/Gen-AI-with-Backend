# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".
from datetime import date
current_date = date.today()
print(current_date.strftime("%Y-%m-%d"))


# Write a program that takes a birth year as input and calculates the age of a person.
from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    age = current_year - birth_year
    return age

birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
print("You are", age, "years old.")


# Create a program that calculates and prints the number of days remaining until a person's next birthday.
# take users birth date as input
from datetime import date, datetime

def days_until_next_birthday(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, "%m/%d/%Y").date()
    today = date.today()
    next_birthday = date(today.year, birth_date.month, birth_date.day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)
    days_remaining = (next_birthday - today).days
    return days_remaining

birth_date_str = input("Enter your birth date (MM/DD/YYYY): ")
days_remaining = days_until_next_birthday(birth_date_str)
print("There are", days_remaining, "days remaining until your next birthday.")


# Write a program that calculates and displays the number of days between two given dates.
from datetime import datetime

def days_between_dates(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, "%m/%d/%Y").date()
    date2 = datetime.strptime(date_str2, "%m/%d/%Y").date()
    delta = abs(date2 - date1)
    return delta.days

date_str1 = input("Enter the first date (MM/DD/YYYY): ")
date_str2 = input("Enter the second date (MM/DD/YYYY): ")
days_difference = days_between_dates(date_str1, date_str2)
print("The number of days between the two dates is:", days_difference)


# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).
from datetime import datetime

def get_day_of_week(date_str):
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    day_of_week = date_obj.strftime("%A")
    return day_of_week

date_str = input("Enter a date (MM/DD/YYYY): ")
day_of_week = get_day_of_week(date_str)
print("The day of the week for", date_str, "is:", day_of_week)



# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.
from datetime import datetime, timedelta

def calculate_future_date(start_date_str, days):
    start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
    future_date = start_date + timedelta(days=days)
    future_date_str = future_date.strftime("%m/%d/%Y")
    return future_date_str

start_date_str = input("Enter the starting date (MM/DD/YYYY): ")
days = int(input("Enter the number of days in the future: "))
future_date_str = calculate_future_date(start_date_str, days)
print("The date", days, "days from", start_date_str, "is:", future_date_str)



#Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.
from datetime import datetime, timedelta

def calculate_future_date(start_date_str, days):
    try:
        start_date = datetime.strptime(start_date_str, "%m/%d/%Y")
        future_date = start_date + timedelta(days=days)
        future_date_str = future_date.strftime("%m/%d/%Y")
        print("The date", days, "days from", start_date_str, "is:", future_date_str)
    except ValueError:
        print("Invalid date format. Please enter the date in MM/DD/YYYY format.")

# Example usage
start_date_str = input("Enter the starting date (MM/DD/YYYY): ")
days = int(input("Enter the number of days in the future: "))
calculate_future_date(start_date_str, days)


# Write a Python program that uses the datetime module to print the current date and time.
from datetime import datetime

current_datetime = datetime.now()
print("Current date and time:", current_datetime)
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted current date and time:", formatted_datetime)


# Create a function that takes a datetime object as input and formats it as "Day-Month-Year" (e.g., "25-August-2023") using strftime().
from datetime import datetime

def format_datetime_as_day_month_year(dt):
    formatted_date = dt.strftime("%d-%B-%Y")
    return formatted_date

now = datetime.now()
formatted_date = format_datetime_as_day_month_year(now)
print("Formatted date:", formatted_date)

