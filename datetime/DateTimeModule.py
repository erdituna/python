
import datetime 

def days_in_month(year, month):

    if month<=7 and month%2!=0:
        return 31
    elif month>7 and month%2==0:
        return 31
    elif month!=2:
        return 30
    else:
        if ((year%4== 0 and year%100!=0)or(year%400==0)):
            return 29
        else:
            return 28
        
def is_valid_date(year, month, Days):
    
    
    if datetime.MINYEAR <= year <= datetime.MAXYEAR :
        if 0 < month <= 12:
            check_day = days_in_month(year, month)
            if ((Days <= check_day) and (Days>0)):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
   
    if (is_valid_date(year1, month1, day1) and
        is_valid_date(year2, month2, day2) ):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        if date1 < date2 :
            dif = date2 - date1
            return dif.days
        else:
            return 0
    else:
        return 0 
    

def age_in_days(year, month, Day):
  
    valid = is_valid_date(year, month, Day)
    
    if (valid == True):
        date = datetime.date(year, month, Day)
    else:
        return 0
    todays_date = datetime.date.today()
    if (valid == False):
        return 0
    if date > todays_date:
        return 0
    else:
        days_age = todays_date - date
        return (days_age.days)

print(type(days_between(2015,5,5,2014,5,6)))   
print((days_between(2015,5,5,2014,5,6)))
print(age_in_days(1996,5,19))
print(days_in_month(1,1))
    
