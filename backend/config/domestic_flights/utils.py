from datetime import datetime

def get_weekday(date_str):
    # Assuming date_str is in the format 'YYYY-MM-DD'
    date_object = datetime.strptime(date_str, '%Y-%m-%d')
    # strftime('%A') returns the full weekday name
    return date_object.strftime('%A')
