import datetime
import time
#defines message objects to assist with parsing

class Message:
    # class attribute
    date_format = "%b %d, %Y %I:%M%p"
    def __init__(self, timestamp, contents, author):
        self.timestamp = time.strptime(str, Message.date_format)
        self.timestamp_cmp = time.mktime(self.timestamp)
        self.contents = contents
        self.author = author


#test
str = "Nov 29, 2017 9:19am"
x = datetime.datetime.strptime(str)
time.strptime(str,"%b %d, %Y %I:%M%p")
y = time.mktime(x)