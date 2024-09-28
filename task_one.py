import datetime

def get_days_from_today(date):
    """
    DOCSTRING
    argument:
    date -- accepts a date in the format "YYYY-MM-DD"

    output:
    The difference in days between the given date and today's date.
    """
    while True:
        try:
            date_today = datetime.datetime.today()
            object_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            result_didd_days = date_today - object_date
            return f"Difference of days is: {result_didd_days.days}."
        except ValueError:
            messenge = f"time data {date} does not match format '%Y-%m-%d'"
            print(messenge, "\n", "-" * len(messenge), sep="")
            date = input("Enter the date in the format YYYY-MM-DD: ")
        
    
input_date = input("Enter the date in the format YYYY-MM-DD: ")
print(get_days_from_today(input_date))