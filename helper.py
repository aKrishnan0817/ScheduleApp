from datetime import datetime
from dictionary import *

def time():
    dayOfWeek = int(datetime.today().weekday())
    daysLst = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    dayOfWeek = daysLst[dayOfWeek]
    ct = datetime.now().hour*60+datetime.now().minute
    period = 1
    #find the curr period of the day

    periods = [i(8,30),i(9,15),i(10,0),i(10,45),i(10,55),i(11,40),i(12,25),i(13,10),i(13,55),i(14,40)]
    for idx in range(len(periods)-1):
        if ct >= periods[idx] and ct <= periods[idx+1]:
            period = idx+1

    timeData = {
        "day":dayOfWeek,
        "hour": str(datetime.now().hour),
        "minute": str(datetime.now().minute),
        "period": period
    }
    return timeData
def i(h,m):
    return h*60+m
