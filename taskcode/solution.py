from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %z"

def get_month(month):
    months = {
            'Jan':1,
            'Feb':2,
            'Mar':3,
            'Apr':4,
            'May':5,
            'Jun':6,
            'Jul':7,
            'Aug':8,
            'Sep':9,
            'Oct':10,
            'Nov':11,
            'Dec':12,
        }
    return str(months[month])

def days_difference(d1,d2):
    d1 = datetime.strptime(d1,fmt)
    d2 = datetime.strptime(d2,fmt)
    return abs((d2-d1).total_seconds())


def main(a,b):
    
    # a = input()
    # b = input()
    a=a.split()
    b=b.split()
    d1 = a[3]+'-'+get_month(a[2])+'-'+a[1]+' '+a[4]+' '+a[5]
    d2 = b[3]+'-'+get_month(b[2])+'-'+b[1]+' '+b[4]+' '+b[5]

    return (int(days_difference(d1,d2)))
    