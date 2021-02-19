"""A vaccination calculator."""

__author__ = "730331250"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...


population = int(input("Population:"))
doses_administered = int(input("Doses administered:"))
doses_per_day = int(input("Doses per day:"))
target_percent_vaccinated = int(input("Target_percent vaccinated:"))

doses_administered2 = ((float(doses_administered) / 2)) 
doses_per_day2 = ((float(doses_per_day / 2)))

population_percent = float(((target_percent_vaccinated * .01) * population))
difference = population_percent - doses_administered2
days_until = round(difference / doses_per_day2)

print(">>>>" + str(days_until))

print("Population:" + (str(population)))
print("Doses administered:" + str(doses_administered2))
print("Doses per day:" + str(doses_per_day2))
print("Target percent vaccinated:" + str(target_percent_vaccinated))

today: datetime = datetime.today()
dayz: timedelta = timedelta(float(days_until))
tomorrow: datetime = today + dayz
future = (tomorrow.strftime("%B %d, %Y"))

print(f"We will reach {target_percent_vaccinated}% vaccination in {days_until} days, which falls on {future}.")