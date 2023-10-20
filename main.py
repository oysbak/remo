from datetime import datetime


def get_day_name():
    date_obj = datetime.utcnow()
    day_name = date_obj.strftime('%A')
    return day_name


def get_month_name():
    date_obj = datetime.utcnow()
    month_name = date_obj.strftime('%m')
    return month_name