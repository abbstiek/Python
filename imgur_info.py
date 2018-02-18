"""     Abygail Stiekman
        aes15d
        imgur_info.py"""


from __future__ import print_function
import requests, json

"""This program will gather and scrape user's comment information
from Imgur using both json and requests"""


class imgur_info(object):

    user = ""
    json_ex= ""

    def __init__(self):

        self.username()

    def username(self):

        #prompts user to enter username, will be used to
        #look up user's page w/json
        self.user = raw_input("Enter a username: ")

    def load_info(self):

        # will be used to append user data
        my_list = []
        #runs 500x
        for i in xrange(0, 500):
            url = requests.get("http://imgur.com/user/" + self.user + \
                "/index/newest/page/" + str(i) + "/hit.json?scrolling")
            # if it is empty or does not load, end function
            if not url.content.strip() or url.status_code != 200:
                break
            else:
                #load json to append information
                self.json_ex = json.loads(url.content)
                #gets information found after these
                for data in self.json_ex["data"]["captions"]["data"]:
                    # append data to my_list
                    my_list.append(
                        [data["hash"],
                        data["points"],
                        data["title"],
                        data["datetime"]])
        # if list is empty, returns
        if not my_list:
            return my_list
        #sorts the user's points from highest to greatest
        my_list.sort(key=lambda x: int(x[1]), reverse=True)
        #returns sorted user's comments
        return my_list

    def print_data(self, data):
        #assigns pulled information to variable "fun"
        fun = data
        #if data is found,
        if fun:
            #prints top 5 comments based on points
            if len(fun) > 5:
                length = 5
            else:
                #done if the user doesn't have 5 comments
                length = len(fun)
                #prints data from load_info depending on # of comments
            for i in range(0, length):
                print(str(i + 1) + ". " + fun[i][0])
                print("Points:", fun[i][1])
                print("Title:", fun[i][2])
                print("Date:", fun[i][3])
                print()
        #if no data is found, whether its comments or the user
        else:
            print("user doesn't exist or hasn't posted any comments.")


if __name__ == "__main__":
    #sets imgur_info function
    start = imgur_info()
    #links information with imgur page
    load_data = start.load_info()
    #runs both page and data together and prints users information,
    #if applicable
    start.print_data(load_data)
