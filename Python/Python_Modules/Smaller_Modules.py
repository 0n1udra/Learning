import getpass as gp

import urllib as url

import datetime as dt

import pytz
##### getpass ##### ---------------------------------------

def get_Password(): pass

# urllib
def web_Image_Downloader():
    pass

def dateTime():
    today = dt.datetime.today() # gets the current date and time, no time-zone or daylight savings(this is naive time)
    todaysDate = dt.datetime.today().date() # gets current date, also naive date/time
    todaysTime = dt.datetime.today().time() # gets current time, also naive date/time

    print("today|", today) # prints todays date and time from today
    print("today.day|", today.day) # prints out only the day from today
    print("today.weekday()|", today.weekday()) # prints out the day of the week number
    # Monday = 0 .... Sunday = 6
    print("today.isoweekday()|", today.isoweekday()) # prints out the day of the week also but starts at 1
    # Monday = 1 .... Sunday = 7

    # (Y, D, M, H, m, S, ms, tzinfo)
    tdDay = dt.datetime(2017, 3, 3, 15, 35, 54) # (year, date, month, hour, minutes, seconds) or (hour=, second=, minute=, month=, day=, year=) keywords args don't have to be in order
    # you can input your own date and time, make sure there's no leading 0 in single digits ex. 03 vs 3 , this is for any arg
    tdTime = dt.time(minute=12, hour=15, second=53, microsecond=530000) # sets custom time, without keyword args (hour, minutes, second, microseconds, tzinfo)
    tdDT = dt.datetime(day=13, month=11, year=2017) # custom date, without keyword args (year, date, month)
    # you can also use keyword args with datetime or use this format (year, date, month, hours, minutes, seconds, microseconds, tzinfo)
    # whether your using keyword args or the regular format, you do need to input HMS for time and YDM for date and YMDHMS for datetime,
    #  on either of these the there's optional ones, like tzinfo and microseconds
    print("tdDay|", tdDay)
    print("tdTime|", tdTime)
    print("tdDT|", tdDT)
    # prints specified dates and times

    # ----- Accessing and Editing specific info -----
    # accessing individual thing from datetime vars
    tdDayDay = tdDay.day
    tdDayMonth = tdDay.month
    tdDayYear = tdDay.year
    # access certain thing from tdDay
    tdTimeHour = tdTime.hour
    tdTimeMinutes = tdTime.minute
    tdTimeSeconds = tdTime.second
    tdTimeMSecs = tdTime.microsecond
    # same as tdDay but this is accessing time info

    todayDate = today.date()
    todayTime = today.time()
    todayCTime = today.ctime() # this prints out shortened worded version, so Mon - Sun for days and Jan - Dec for months, Ex >
        # Thu Mar 16 11:05:17 2017
    todayTStamp = today.timestamp()
    todayTimeTuple = today.timetuple() # returns all the data in a tuple, Ex. >
        # time.struct_time(tm_year=2017, tm_mon=3, tm_mday=16, tm_hour=11, tm_min=7, tm_sec=32, tm_wday=3, tm_yday=75, tm_isdst=-1)
    # you can still use the stuff from above like today.day/month/minute/etc, but you can get more info with a method like time() well return HMS from today
    # date() well return the date, and then there's othor useful methods also

    todayNewDT = today.replace(2017, 12, 4, 14, 42, 53) # as you can see this didn't update the tzinfo or microseconds, but it'll still work
    # this well change the YMD,HMS in today
    print("todayNewDT|", todayNewDT)
    todayNewTime = today.time().replace(22, 12, 35)
    # this well only update the time, works with today.date() also, or just do today.replace() for the whole thing
    todayNewDate = today.replace(day=3, month=8, year=2018)
    # you can use keyword args to update specific things, also works with today.time()/date().replace()
    # the program well crash and tell you if you day is out of range for a month or time is impossible, or something like that


    # ----- timedelta -----
    kirbyBdayDate = dt.date(day=25, month=12, year=2017)
    # this shows you can use keyword args also, if you don't you do have to input in order (year, day, month)
    print("KirbyBday|", kirbyBdayDate) # prints kirbyBday
    till_Bday = kirbyBdayDate - todaysDate
    # subtracts kirbyBday from todays current date, and returns a timedelta
    print("till_Bday|", till_Bday)
    # this well return how many days left
    print("till_Bday in seconds| {:,}".format(till_Bday.total_seconds()))
    # this well print till_Bday in seconds, I used {:,} and .format() so it separated the number in sections; so it didn't look something like this > 24537600.0 vs 24,537,600.0


    # -----  Time-Zones and pytz -----
    myTZ = today.replace(tzinfo=pytz.UTC)
    # you can add the time zone to the today var
    todaysTZ = dt.datetime.today().replace(tzinfo=pytz.UTC)
    # you can also just add it to today()
    # you can also specify it when creating the date() or time() or datetime(), datetime(Y, D, M, H, M, S, tzinfo=pytz.timezone('location/timezon'))
    print("myTZ|", myTZ)
    print("todaysTZ|", todaysTZ)


    myTZUpdated = myTZ.astimezone(pytz.timezone('US/Eastern')) # updates timezone, you could also just just .replace(tzinfo=)
    print("myTZUpdated|", myTZUpdated)


    naiveDT = dt.datetime.today() # creates a naive datetime(something that doesn't have daylight or timezone awareness)
    estTZ = pytz.timezone('US/Eastern') # makes a new timezone
    myTZLocalized = estTZ.localize(naiveDT) # uses localize() to basicallyu update the naiveDT
    print("myTZLocalize|", myTZLocalized)
    # this well crash if datetime already has a timezone or it's not naive. if it already has timezone use .astimezone() or .replace(tzinfo=)

    print("\n"*5)
    def get_All_Timezones():
        for tz in pytz.all_timezones: print(tz)
        # this well loop through and print out all the time zones available

    def get_All_UStz():
    # get all the us timezones
        for UStz in pytz.all_timezones:
            splitTZ = UStz.split("/") # splits it up by the slash, so you have the country/etc then the timezone
            if splitTZ[0] == 'US': print(UStz)
            # if it's a US timezone, then it'll print out that timezone. you can of course change the 'US' to something different


    # ----- Printing -----
    # Date = dt.datetime(2017, 3, 15, 11, 35, 55) # sets date and time. Year, Month, Day, Hour, Minute, Second
    # you can input your own data like above, put i'm going to use the current relavent date and time with .now()
    Date = dt.datetime.now()
    print("Datetime|", Date)  # prints out date and time in this format Y-M-D H:M:S

    print("Datetime Formatted| {:%B %d %Y, %X}".format(Date))  # formats the date as specified,
    # common ones to use. Month  -- %B - full month name (January) %b small Month name (Jan),  %j - the day number of the year (50 or 360)
    # Day  --  %d - day of moth,  %A full Day name(Monday),  %a shortened Day name(Mon)
    # Year  --  %Y - full year (2017),  %y - shortened year (17)
    # Time  --  %X - Time (11:35:55),  %H - 24h Hour,  %I - 12h Hour,  %M - Minutes, %S, Seconds, %f - microseconds
    # All  --  %c everything (Wed Mar 15 11:35:55 2017),  %x - date (03/15/17),

    print("Datetime Formatted with text| Today is {0:%A} on {0:%B %d}, the {0:%j} day of the year. And the time is {0:%X}".format(Date))
    # you can add text and move the data around like this to give a full sentence with the date and time. you do need the 0 part in {0:%j}, since that says get data from Date


    print("strftime|", Date.strftime("today is %c")) # convets datetime to string
    # you can use strftime() to basically do what print is doing above in the {}

    wordedDate = 'today is Wednesday March 15, 2017'
    print("strptime|", dt.datetime.strptime(wordedDate, "today is %A %B %d, %Y")) # converts string to datetime
    # this well convert a string input into a datetime datetime, you have to use the % to tell datetime what format your using, so %A %B %d, %Y is day name, month name, day, then year
    # you can add text(I would say don't) but then you'll have to input the same text in with the % in the second arg in .strptime()


    convertedDT = dt.datetime.strptime(wordedDate, "today is %A %B %d, %Y")
    # if you want to you can also put it in a var, then you can do datetime operations like any other
dateTime()