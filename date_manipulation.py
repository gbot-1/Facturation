from datetime import datetime, timedelta
import babel.dates

# Set locale to French
# locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

def convert_date_to_text(date_str):
    date_object = datetime.strptime(date_str, '%d/%m/%Y')

    # Format date to '08 août 2024'
    formatted_date = babel.dates.format_date(date_object, format='d MMMM yyyy', locale='fr')
    return formatted_date

def compute_days_difference(date_str):
    """
    Compute the number of days between today and the 14 days span of the input date.
    """
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    today = datetime.now()
    span_end_date = date_obj + timedelta(days=14)
    
    # Calculate the difference in days
    difference_in_days = (span_end_date - today).days
    return difference_in_days

def determine_quadrimester(date_str):
    """
    Determine the quadrimester (Q1, Q2, Q3, Q4) based on the input date.
    """
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    month = date_obj.month
    
    if month in [1, 2, 3]:
        return "Q1"
    elif month in [4, 5, 6]:
        return "Q2"
    elif month in [7, 8, 9]:
        return "Q3"
    elif month in [10, 11, 12]:
        return "Q4"


