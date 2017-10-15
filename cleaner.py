import csv
import sys
# '', '0/0']

f = open("course_details.csv","rb")
data = csv.reader(f,delimiter=';')
data = [row for row in data]
length = len(data)
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
    c_quarter = data[i][5]
    # if not c_quarter == "AU 17WI 18" and not c_quarter == "AU 17" and not c_quarter == "WI 18":
    c_curr = data[i][6].strip
    c_campus = data[i][7]
    c_sec_no = int(data[i][8])+1
    c_sec = data[i][9]
    c_timings = data[i][10]
    # TODO Make parser for class timings
    c_room = data[i][11]
    # TODO Make parser for class rooms
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
