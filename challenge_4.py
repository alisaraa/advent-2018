# # Strategy 1: Find the guard that has the most minutes asleep. What minute does that guard spend asleep the most?
#
# What is the ID of the guard you chose multiplied by the minute you chose?


INPUT = "./sleep_log.text"
data_dict = {}
times = []
# open and read file
lines = open(INPUT).read().splitlines()
for line in lines:
    time = ' '.join(line.split(' ')[0:2])
    description = ' '.join(line.split(' ')[2:])
    data_dict[time] = description

# order the dictionary
awake = True
sleepiness = []
for key, value in sorted(data_dict.iteritems()):
    date = key.split(' ')[0].replace('[', '')
    minute = key.split(' ')[1].replace(']', '')
    if value.startswith('Guard'):
        guard_id = value.split(' ')[1].replace("#", '')
    elif value == 'falls asleep':
        awake = False
    elif value == 'wakes up':
        awake = True
    #print(key, value)
    sleepiness.append([date, minute, guard_id, awake])

guards = {}
for awake in range(len(sleepiness)-1):
    sleep_minutes = []
    if sleepiness[awake][3]== False:
        guard = int(sleepiness[awake][2])
        minute_asleep = int(sleepiness[awake][1].split(':')[1]) # minute they fell asleep up
        minute_awake = int(sleepiness[awake + 1][1].split(':')[1]) # minute they woke up
        for x in range(minute_asleep, minute_awake):
            sleep_minutes.append(x)
        if guards.get(guard) is not None:
            guards[guard] = guards[guard] + sleep_minutes
        else:
            guards[guard] = sleep_minutes

for guard, minutes in sorted(guards.iteritems(), key=lambda (k,v): (len(v),k)):
    highest_guard = guard

minute_freq = {}
for  minute in guards[highest_guard]:
    minute_freq[minute] = minute_freq.get(minute, 0) + 1

for key, value in sorted(minute_freq.iteritems(), key=lambda (k,v): (v,k)):
    highest_minute = key

# print(highest_guard * highest_minute)
# print(highest_minute)

# part 2

highest_value = 0
for guard, minutes in guards.iteritems():
    minute_freq = {}
    print(guard)
    for min in minutes:
        minute_freq[min] = minute_freq.get(min, 0) + 1
    for key, value in sorted(minute_freq.iteritems(), key=lambda (k,v): (v,k)):
        print(key, value)
        highest_minute = key
        count_times = value
    if count_times > highest_value:
        highest_value = count_times
        minute = highest_minute
        highest_guard = guard
print(highest_guard * minute)
