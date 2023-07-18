# The time module provides a function, also named time , that returns the current
# Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point. On
# UNIX systems, the epoch is 1 January 1970.
# >>> import time
# >>> time.time()
# 1437746094.5735958
# Write a script that reads the current time and converts it to a time of day in hours, minutes, and
# seconds, plus the number of days since the epoch.

import time

epoch = time.time()
seconds_in_a_day = 24 * 60 * 60
seconds_in_an_hour = 60 * 60
seconds_in_a_minute = 60

days = epoch // seconds_in_a_day
hours = (epoch % seconds_in_a_day) // seconds_in_an_hour + 8
minutes = (epoch % seconds_in_a_day) % seconds_in_an_hour // seconds_in_a_minute
seconds = (epoch % seconds_in_a_day) % seconds_in_an_hour % seconds_in_a_minute
print("Current time is %d: %d: %d: %d" %(days, hours, minutes, seconds)) 

# output
# python3 assign5.1/question1.py
# Current time is 19556: 17: 25: 58