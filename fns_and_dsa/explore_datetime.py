import datetime
from datetime import timedelta  # Uncomment and use this import


def display_current_datetime():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"Current Date and Time: {current_date}\n")


def calculate_future_date():
    number_of_days = int(
        input("Enter the number of days to add to the current date:"))
    future_date = datetime.datetime.now() + timedelta(days=number_of_days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date: {formatted_future_date}")


display_current_datetime()
calculate_future_date()
