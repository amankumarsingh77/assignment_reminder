import time

current_time_unix = int(time.time())

one_hour_before_unix = current_time_unix - 7200
print("Current Time (Unix timestamp):", current_time_unix)
print("1 Hour Before (Unix timestamp):", one_hour_before_unix)
