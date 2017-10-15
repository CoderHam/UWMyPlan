import codecs
import csv

with open('course_details.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter = ';')
    text_file = open("course_details.txt", "r")
    deliminator = ";;"
    c_links = text_file.readlines()
    for i in range(1,len(c_links)):
        if c_links[i].startswith("PCE"):
            c_links[i-1] = c_links[i-1].strip("\n")+c_links[i].strip("PCE")
        if not c_links[i-1].startswith("PCE"):
            row_c = c_links[i-1].split(deliminator)[:-1]
            wr.writerow(row_c)
