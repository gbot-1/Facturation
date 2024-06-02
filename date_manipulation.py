from datetime import datetime, timedelta
import locale

# Set locale to French
locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

def convert_date_to_text(date_str):
    """
    Convert a date string in the format "DD/MM/YYYY" to "DD month YYYY" in French.
    """
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    print(date_obj.strftime("%B"))
    return date_obj.strftime("%d %B %Y")

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


