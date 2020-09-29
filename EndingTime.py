# expressed in a 24-hour clock with leading zeroes, like 08:30 or 14:07
startingTime = input()
# duration in minutes
duration = int(input())

# the input format is fixed as ##:##, so ":" is at index 2
hour = int(startingTime[0:2])
minute = int(startingTime[3:])

finalMinute = (duration + minute) % 60
finalHour = (hour + (duration + minute) // 60) % 24

# all times should be formatted as numbers between 00:00 and 23:59
print('{:02d}'.format(finalHour) + ':' + '{:02d}'.format(finalMinute))
