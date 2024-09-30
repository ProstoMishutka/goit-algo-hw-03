import datetime

def get_days_from_today(date):
    """
    DOCSTRING
    argument:
    date -- accepts a date in the format "YYYY-MM-DD"

    output:
    The difference in days between the given date and today's date.
    """
    try:
        date_today = datetime.datetime.today()
        object_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        result_didd_days = date_today - object_date
        return result_didd_days.days
    except ValueError:
        print("The data is incorrect.")
    
    
print(get_days_from_today("2024-11-01"))