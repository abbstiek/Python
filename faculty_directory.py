"""Abygail Stiekman

aes15d

faculty_directory.py"""

from __future__ import print_function
from bs4 import BeautifulSoup
import requests


"""Faculty_directory.py scrates the FSU CS faculty website.
	The faculty's name, office, telephone number,
	and e-mail address are pulled from the website
	and there are some special cases as well as
	panama city campus faculty on the website"""


class facdirectory(object):
    url = ""

    soupy_soup = None

    page = None

    def __init__(self, url=""):

        self.url = url

    def connect(self):

        self.page = requests.get(self.url).content

    def dir(self):

        #this function will scrape the link from
	#the faculty directory

        soupy_soup = BeautifulSoup(self.page, 'html.parser')
        # pulls all 'td' tags - indicator of staff url
        directory_array = soupy_soup.find_all('td')
	#if faculty is found,pull information from website
        for i in directory_array:
            tag = i.find('a')
            #this will gather needed info to later print staff details
            self.print_info(tag.next_sibling.next_sibling.next_sibling['href'])

    def null_filler(self, fun_arr):

        ##this function will append the information that we are trying to collect
	##if the information is not available, then we will need to print "N/A"

	#list to hold appended info
        data = []

        for p_row in fun_arr:
	#collects data to be outputted
            output = p_row.text.encode('utf-8').strip()
            if not output:
		#if there is no information to scrape for the given category
                output = "N/A"
                data.append(output)
            else:
		#if there is data, append it.
                data.append(output)
	#returns information to be printed in get_info
        return data

    def print_info(self, link):

	##this function will crawl the faculty pages and
	#navigate to find the necessary td tags
	#to correctly print the data when necessary

       	page = requests.get(link).content
        soupy_soup = BeautifulSoup(page, 'html.parser')
        fun_arr = soupy_soup.find_all('td')
        info = []
        if len(fun_arr) >= 6:
            #if employee is on the main campus, will fill list
            info = self.null_filler(fun_arr)
            name = soupy_soup.select_one(".main_title")
		##will print out all fsu-main campus employees
	    print("Name:", name.text.encode('utf-8'))
            print(info[0], " ", info[1])
	    print(info[2], info[3])
	    print(info[4], info[5])
	    print("****************************************", sep="")
        else:
            #if employee is on panama city campus, will fill list
            fun_arr = soupy_soup.find_all('div', attrs={'class': 'field--item'})
            info = self.nullfiller(fun_arr)
            #tag for page header class
            name = soupy_soup.select_one(".page-header")
		##will print out all fsu panama city campus employees
	    print("Name:", name.text.encode('utf-8'), end="")
            print("Office: ", info[5])
	    print("Telephone: ", info[6])
            print("E-Mail: ", info[7])
	    print("****************************************", sep="")

if __name__ == "__main__":
    #runs class with cs faculty page
    start = facdirectory("http://www.cs.fsu.edu/department/faculty/")
    #begins function connect() from class facdirectory
    start.connect()
    #begins function dir() from class facdirectory
    start.dir()
