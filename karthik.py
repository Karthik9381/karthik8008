from datetime import date
from datetime import time
from datetime import datetime
def main():
    today = date.today()
    print("today",today)
    print("Date components: ",today.day,today.month,today.year)
    days = ["mon","tue","wed","thu","fri","sat","sun"]
    print("Which is a:",days[today.weekday()])
    karthik = datetime.now()
    print("The current date and time is",karthik)
main()
