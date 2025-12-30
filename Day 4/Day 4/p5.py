#The year is leap year or not
year=int(input("Enter the year:"))
def is_leap(year):
    if year%4==0 and year%100!=0 or year%400==0:
        print(f"The {year} is Leap")
    else:
        print(f"The {year} is Not Leap")
is_leap(year)