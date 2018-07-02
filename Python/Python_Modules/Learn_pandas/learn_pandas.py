import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import calendar

# https://github.com/QCaudron/pydata_pandas  --  based from

# Temporary fix to print() not showing newline at the end
nl = "\n"


coffeeData = pd.read_csv("data/coffees.csv")

# ===== Showing Data =====


# Print first 5 rows(data entries). .head([amount]) / .tail([amount])
print(coffeeData.head(), nl)
# NaN - Not a Number

# Shows second entry of data. .iloc[x]
print("Entry 1:\n", coffeeData.loc[1], nl)

# Shows different data info ex. freq, count, top, etc
print("line 22:\n", coffeeData.describe(), nl)

# Shows all data entries where the coffees column is null (NaN, etc)
print("All NaN entries:\n", coffeeData[coffeeData.coffees.isnull()], nl)

# Shows data types
print("Data types:\n", coffeeData.dtypes, nl)

# Prints first timestamp object and shows what object type it is
print("timestamp[0]:\n", coffeeData.timestamp[0])
print("timestamp[0] type:\n", type(coffeeData.timestamp[0]), nl)


# ===== Setup =====

print("coffees column to numeric\nBefore:\n", coffeeData.head())
print(coffeeData.dtypes, nl)
# Sets coffees data to numeric and set anything else to NaN

coffeeData.coffees = pd.to_numeric(coffeeData.coffees, errors="coerce")

print("After:\n", coffeeData.head())
print(coffeeData.dtypes)
print("coffees[0] type:\n", type(coffeeData.coffees[0]), nl)



# Drops NaN entries inplace, instead of making a copy. This will also drop the index corresponding to the dropped NaN
coffeeData.dropna(inplace=True)
print("Drop NaN:\n", coffeeData.head(), nl)

# Converts to int64 instead of float64. put after .to_numeric and .dropna() to not encounter type conflict
coffeeData.coffees = coffeeData.coffees.astype(int)

coffeeData.timestamp = pd.to_datetime(coffeeData.timestamp)
print("timestamp column to datetime:\n", coffeeData.dtypes, nl)

print(coffeeData.describe(include="all"), nl)

# Only data that is before specified data. pandas automatically converts string to datetime for boolean expression
coffeeData = coffeeData[coffeeData.timestamp < "2013-03-01"]
print("data entries before 2013-03-01\n", coffeeData.tail(), nl)

# Shows # of occurrences in contributor
print("Contributor count:\n", coffeeData.contributor.value_counts())

# Adds weekday column to data frame using datetime.weekday_name
coffeeData = coffeeData.assign(weekday=coffeeData.timestamp.dt.weekday_name)
print("Added weekday to data frame:\n", coffeeData.head(), nl)

# Groups data by weekday then sorts by weekday name. How many entries on given day
cData_weekdayGrouped = coffeeData.groupby('weekday').count()
cData_weekdayGrouped = cData_weekdayGrouped.loc[list(calendar.day_name)]
print("Grouped by weekday:\n", cData_weekdayGrouped.head())



# ===== Plotting =====

plt.rcParams['axes.grid'] = True # Enables grid for all

# This will plot x: index and y: coffees. not exactly what we want
#coffeeData.coffees.plot()


# Show both plots in one window
fig1, axes = plt.subplots(nrows=1, ncols=2, figsize=(13, 5), num="Coffee Data")

coffeeData.plot(x='timestamp', y='coffees', style='.-', title="Time x Coffees", ax=axes[0], grid=True)

coffeeData.contributor.value_counts().plot(kind='bar', title="Contributor x Times", ax=axes[1])

# New window. on newer Macs it'll open a new tab
fig2 = plt.figure()
# Bar graph of how many days by weekday
cData_weekdayGrouped.coffees.plot(kind='bar')







plt.show()


