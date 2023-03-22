seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
seconds_in_full_day = 60 * 60 * 24
full_days = [second // seconds_in_full_day for second in seconds]
print(full_days)