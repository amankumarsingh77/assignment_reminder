from datetime import datetime
import pytz
import time
def time_convertor(timestamp):

    ist_timezone = pytz.timezone('Asia/Kolkata')
    ist_date_time = datetime.fromtimestamp(timestamp, tz=pytz.utc).astimezone(ist_timezone)

    formatted_ist_date_time = ist_date_time.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_ist_date_time

def time_from_to():
    time_from = int(time.time())
    time_to = time_from + (7 * 24 * 3600)
    return  time_from, time_to
