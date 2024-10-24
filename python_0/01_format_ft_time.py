# import the time module
import time

"""
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
"""

# get the current time in seconds since the epoch
seconds = time.time()
formatted_val = f"{seconds:,.4f}"
scientific_notation = "{:.3e}".format(seconds)
print("Seconds since January 1, 1970:", formatted_val, "or", scientific_notation, "in scientific notation")

# convert the time in seconds since the epoch to a readable format
local_time = time.ctime(seconds)


result = time.localtime(seconds)

time_string = time.strftime("%b %d %Y", result)

print(time_string)

"""
Seconds since epoch = 1727292119.42275
Local time: Wed Sep 25 21:21:59 2024
result: time.struct_time(tm_year=2024, tm_mon=9, tm_mday=25, tm_hour=21, tm_min=21, tm_sec=59, tm_wday=2, tm_yday=269, tm_isdst=1)
"""

