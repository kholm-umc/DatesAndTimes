"""
Author: Ken Holm
Purpose: Demonstrate some of the python date and time functions
         See https://docs.python.org/3.7/library/datetime.html?highlight=datetime#module-datetime
"""

import datetime


def hold(info, label="", ask=False):
    """
    Print some info and pause

    :param info: An object that will be printed
    :type info: various object
    :param label: A label that will be printed
    :type label: str
    :param ask: Should we pause or not?
    :type ask: bool
    """
    if (label):
        print(label)

    print(info)

    if (ask):
        input(f"Continue: ")
        print("==================================================")

    print()


rightNow = datetime.datetime.now()

hold(rightNow, "Default local datetime object", True)

hold(datetime.datetime.utcnow(), "Default UTC datetime object", True)

"""
What is epoch time?

What about January 19, 2038 at 3:14a?

 See https://www.unixtimestamp.com/index.php
"""
hold(rightNow.timestamp(), "Default timestamp", True)

hold(rightNow.year, "Just the year", True)

hold(rightNow.month, "Just the month", True)

hold(rightNow.day, "Just the day", True)

"""
We can create a datetime object with a specific date and time
"""

myBirthday = datetime.datetime(1987, 6, 5, 4, 3, 21)

hold(myBirthday, "Default datetime object", True)

"""
What about the difference in dates and times?
"""

dateDifference = rightNow - myBirthday

hold(dateDifference.days, "Difference between now and my birthday in days", True)

"""
We can format our datetime object, too
 See https://docs.python.org/3.7/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior
"""

hold(rightNow.strftime("%a"), "rightNow.strftime('%a'): just weekday, short version", True)

hold(rightNow.strftime("%A"), "rightNow.strftime('%A'): just weekday, full version", True)

hold(rightNow.strftime("%w"), "rightNow.strftime('%w'): just weekday as a number 0-6, 0 is Sunday", True)

hold(rightNow.strftime("%d"), "rightNow.strftime('%d'): just day of month 01-31", True)

hold(rightNow.strftime("%b"), "rightNow.strftime('%b'): just month name, short version", True)

hold(rightNow.strftime("%B"), "rightNow.strftime('%B'): just month name, full version", True)

hold(rightNow.strftime("%m"), "rightNow.strftime('%m'): just month as a number 01-12	12", True)

hold(rightNow.strftime("%y"), "rightNow.strftime('%y'): just year, short version, without century", True)

hold(rightNow.strftime("%Y"), "rightNow.strftime('%Y'): just year, full version", True)

hold(rightNow.strftime("%H"), "rightNow.strftime('%H'): just hour 00-23 (i.e., 24-hour clock)", True)

hold(rightNow.strftime("%I"), "rightNow.strftime('%I'): just hour 00-12 (i.e., 12-hour clock)", True)

hold(rightNow.strftime("%p"), "rightNow.strftime('%p'): just AM/PM", True)

hold(rightNow.strftime("%M"), "rightNow.strftime('%M'): just minute 00-59", True)

hold(rightNow.strftime("%S"), "rightNow.strftime('%S'): just second 00-59", True)

hold(rightNow.strftime("%f"), "rightNow.strftime('%f'): just microsecond 000000-999999", True)

hold(rightNow.strftime("%j"), "rightNow.strftime('%j'): just day number of year 001-366", True)

hold(rightNow.strftime("%U"), "rightNow.strftime('%U'): just week number of year, Sunday as the first day of week, 00-53", True)

hold(rightNow.strftime("%W"), "rightNow.strftime('%W'): just week number of year, Monday as the first day of week, 00-53", True)

hold(rightNow.strftime("%c"), "rightNow.strftime('%c'): just local version of date and time", True)

hold(rightNow.strftime("%x"), "rightNow.strftime('%x'): just local version of date", True)

hold(rightNow.strftime("%X"), "rightNow.strftime('%X'): just local version of time", True)

hold(rightNow.strftime("%%"), "rightNow.strftime('%%'): just a % character", True)
