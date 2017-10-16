import csv
import sys
import re

f = open("course_details.csv","rb")
data = csv.reader(f,delimiter=';')
data = [row for row in data]
# length = len(data)
data = [list(x) for x in set(tuple(x) for x in data)]

length = len(data)

def parse_time(c_timings):
    times = c_timings.split('<br>')
    days = []
    timings = []
    ampm = []
    if times=='To be arranged':
        return days, timings, ampm
    for t in times:
        all_days = re.split("[^a-zA-Z]*", t)[0]
        days.append(re.findall("[A-Z][^A-Z]*", all_days))
        timings.append(re.findall(r'\d+',t))
        ampm.append(re.split("[^a-zA-Z]*", t)[1:3])
    print days
    print timings
    print ampm
    return days, timings, ampm

def parse_rooms(c_rooms):
    rooms = [r.split(" ") for r in c_rooms.split('<br>')]
    print rooms
    return rooms

# parse_time("MTh8:30 AM - 10:20 PM<br>WT8:30 AM - 10:20 AM")
# parse_rooms("MGH 076<br>SAV 162")

for i in range(0,length):
    c_code = data[i][0]
    try:
        c_credits = int(data[i][2])
        c_title = data[i][1]
    except:
        c_title = data[i][1][:-4]
        c_credits = int(data[i][1][-2:-1])
    c_desc = data[i][3]
    c_prereq = data[i][4]
    c_quarters = data[i][5]
    if len(c_quarters)>5:
        c_quarters = [c_quarters[:5],c_quarters[5:]]
    c_curr = data[i][6].strip()
    c_campus = data[i][7]
    c_sec_no = int(data[i][8])+1
    c_sec = data[i][9]
    c_timings = data[i][10]
    c_rooms = data[i][11]
    c_prof = data[i][12]

# Course Code 0
# Course Title 1
# Course Credit 2
# Description 3
# Prerequisite 4
# Quarter 5
# Curriculum 6
# Campus 7
# Section No 8
# Sec Name 9
# Timings 10
# Classroom 11
# Professor 12
