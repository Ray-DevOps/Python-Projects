
# This program works out whether a given year is a leap year. 
# A normal year has 365 days while leap years have 366 days (an extra day in February).
# A year is a leap year if it is cleanly divisible by 4 but not cleanly divisible by 100, Or
# When it is cleanly divisible by 4, cleanly divisible by 100, and cleanly divisible by 400.

year = 1989

if year % 4 == 0 and year % 100 != 0:
    print(f"The year {year} is a leap year")

elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(f"The year {year} is a leap year")

else:
    print(f"The year {year} is NOT a leap year")
