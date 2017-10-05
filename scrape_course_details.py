from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
import re

driver = webdriver.Chrome('/home/hemant/chromedriver')
driver.get("http://myplan.uw.edu")
time.sleep(4)
driver.find_element_by_class_name('btn-login-netid').click()
username = driver.find_element_by_id("weblogin_netid")
password = driver.find_element_by_id("weblogin_password")

username.send_keys("__username__")
password.send_keys("__password__")
driver.find_element_by_name("submit").click()
time.sleep(4)

# colink = "https://myplan.uw.edu/student/myplan/inquiry?methodToCall=start&viewId=CourseDetails-InquiryView&courseId=a62799c4-b089-48f9-8c60-380066e09e03&courseCd=DATA%20501&sectionFilters={%22queryString%22:%22DATA%22,%22selectedDays%22:[],%22startTime%22:%220630%22,%22endTime%22:%222230%22,%22openOnly%22:false,%22noEnrollmentRestrictionsOnly%22:false,%22noTbaOnly%22:false,%22pceOnly%22:true,%22terms%22:[]}"
def get_course_details(colink):
    driver.get(colink)
    time.sleep(3)

    elem = driver.find_element_by_class_name("pageHeaderText")
    c_title = str(elem.text)
    title_split=c_title.split(" ")
    length = len(title_split)
    e_code = driver.find_elements_by_xpath('//h2[@class="courseDetails__headerText"]')
    c_code = (str(e_code[1].text)).split(" Course")[0]
    c_credits = title_split[-1][1]
    c_title = ""
    for i in xrange(2,length-2):
        c_title = c_title + title_split[i] + " "

    #Description
    e_desc = driver.find_element_by_xpath('//span[@id="u37_control" and @class="uif-readOnlyContent"]')
    c_desc = e_desc.text
    #Prerequisite
    try:
        e_prereq = driver.find_element_by_xpath('//span[@id="u81" and @class="inlineElement uif-boxLayoutHorizontalItem"]')
        c_prereq = e_prereq.text
    except:
        e_prereq = driver.find_element_by_xpath('//span[@id="u78_control" and @class="uif-readOnlyContent"]')
        c_prereq = e_prereq.text
    #Quarter
    e_quarter = driver.find_element_by_xpath('//span[@id="schedule_for_control" and @class="uif-readOnlyContent"]')
    c_quarter = e_quarter.text
    #Curriculum
    e_curr = driver.find_element_by_xpath('//span[@id="u156" and @class="uif-message uif-boxLayoutHorizontalItem"]')
    c_curr = e_curr.text.split(",")[0]
    #Campus
    e_cam = driver.find_element_by_xpath('//span[@id="u157_control" and @class="uif-readOnlyContent"]')
    c_campus = e_cam.text
    e_section = driver.find_elements_by_class_name('courseActivities--primary')
    c_section = len(e_section)
    #Section Data
    if c_section>0:
        elem_list = driver.find_elements_by_class_name("uif-readOnlyContent")
        elem_list=elem_list[4:]
        elem_list = [str(e.text) for e in elem_list]
        elen = len(elem_list)
        sec_list = [elem_list[i:i+(elen/c_section)] for i in xrange(0,elen,elen/c_section)]
        #Professors
        prof_elem_list  = driver.find_elements_by_xpath('//div[@class="removeMargin uif-boxLayoutVerticalItem clearfix"]')
        c_prof_list = [str(prof_elem_list [i*(len(prof_elem_list )/c_section)].text) for i in xrange(0,c_section)]
        #Seats
        seats_elem_list  = driver.find_elements_by_xpath('//div[@class="courseActivities__enrlData--light uif-boxLayoutVerticalItem clearfix"]')
        seats_list =[str(seats.text) for seats in seats_elem_list]
        #Write into a file
        course_details_file = open('course_details.txt', 'a+')
        #Timings
        if len(sec_list[i][1].split("\n"))==1:
            for i in xrange(0,c_section):
                course_details_file.write(c_code+";;")
                course_details_file.write(c_title+";;")
                course_details_file.write(c_credits+";;")
                course_details_file.write(c_desc+";;")
                course_details_file.write(c_prereq+";;")
                course_details_file.write(c_quarter+";;")
                course_details_file.write(c_desc+";;")
                course_details_file.write(c_curr+";;")
                course_details_file.write(c_campus+";;")
                course_details_file.write(str(c_section)+";;")
                #Section Name
                course_details_file.write(sec_list[i][0]+";;")
                #Timings
                course_details_file.write(sec_list[i][1]+";;")
                #Location
                course_details_file.write(sec_list[i][2]+";;")
                #Professor
                course_details_file.write(c_prof_list[i]+";;")
                #Seat Info
                course_details_file.write(seats_list[i]+";;")
                course_details_file.write("\n")

text_file = open("course_links.txt", "r")
c_links = text_file.readlines()
for i in xrange(120,len(c_links)):
    get_course_details(c_links[i])
    print i

driver.quit()
