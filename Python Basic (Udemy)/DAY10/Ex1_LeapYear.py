def isLeap(year):
    # DocString
    """take a year as input and return True or false if it is a leap year."""
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0:
                return True
            else :
                return False
        else :
            return True
    else:
        return False

def daysInMonth(year, month) :
    #DocString
    """take year and month as input and
      return no of days in that month in corresponing year."""
    if month > 12 or month < 1 :
        return "Invalid month"
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(year) and month == 2 :
        return 29
    else :
        return monthDays[month-1]


year = int(input("Enter a year : "))
month = int(input("Enter a month : "))

days = daysInMonth(year=year, month=month)
print(days)