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

def find_all_courses():

    driver.get("http://myplan.uw.edu/course")
    time.sleep(5)
    elem_list = driver.find_elements_by_xpath("//ul/li/a")
    href_list = [str(h.get_attribute("href")) for h in elem_list]
    print href_list

    selected_href_list = [h for h in href_list if h.startswith("https://myplan.uw.edu/course/#/courses?campus=")==True]
    print len(href_list)
    print len(selected_href_list)

    # links_file = open('links.txt', 'w')
    # for hr in selected_href_list:
    #   links_file.write("%s\n" % hr)

def fetch_course_links(clink):
    driver.get("http://myplan.uw.edu/course")
    time.sleep(5)
    driver.get(clink)
    time.sleep(5)
    elem_list = driver.find_elements_by_xpath("//div/span/a")

    href_list = [str(h.get_attribute("href")) for h in elem_list]
    selected_href_list = [h for h in href_list if h.startswith("https://myplan.uw.edu/student/myplan/inquiry?methodToCall=start&viewId=CourseDetails-InquiryView")==True]

    course_links_file = open('course_links.txt', 'a+')
    for hr in selected_href_list:
        course_links_file.write("%s\n" % hr)
    print len(selected_href_list)

def fetch_all_course_links():
    text_file = open("links.txt", "r")
    links = text_file.readlines()
    for link in links:
        fetch_course_links(link)

fetch_all_course_links()

driver.quit()
