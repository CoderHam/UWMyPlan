import pytz
import datetime
import cPickle as pickle
from class_from_timing import find_classes_at_timings

# Get current month, date, weekday
now = datetime.datetime.now()
# now = now + datetime.timedelta(days=90)
# now = now.astimezone(pytz.timezone('America/Los_Angeles'))
daysofweek = ['M','T','W','Th','F']
curr_time = now.hour*100 + now.minute

# if now.hour!=12:
#     curr_time = (now.hour%12)*100 + now.minute
# else:
#     curr_time = 1200 + now.minute
# if now.hour/12<1:
#     curr_mer = 'AM'
# else:
#     curr_mer = "PM"

curr_md = now.month*100 + now.day

#start and end of Autumn and Winter Quarters
Aut = ["AU 17",927,1208]
Win = ["WI 18",103,309]
sems = [Aut,Win]
curr_sem = ""

# Get current semester
for sem in sems:
    if curr_md>=sem[1] and curr_md<=sem[2]:
        curr_sem = sem[0]

curr_weekday = daysofweek[now.weekday()]

print len(find_classes_at_timings(curr_sem, curr_weekday,curr_time))
