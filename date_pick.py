import datetime

try:
    today = input("Enter date as yyyy-mm-dd: ").split("-")
    next_time = int(input("Duration in days: "))
    year, month, day = int(today[0]), int(today[1]), int(today[2])
    given_date = datetime.datetime(year, month, day)
    next_date = str(given_date + datetime.timedelta(days=next_time))
    given_date = str(given_date)

    print('\n\tYour given date is: {}\n\tYour next date is: {}\n'.format(given_date[:11], next_date[:11]))

except ValueError:
    print("\n\tGiven date is Wrong. Check the date and try again.\n")
except Exception as e:
    print("\n\tYou are getting this error: {}\n".format(e))