import datetime
import time
#defines message objects to assist with parsing

class Message:
    # class attribute
    date_format = "%b %d, %Y %I:%M%p"
    group_change_sig = "named the group "
    name_change_sig = "set the nickname for "
    id = 0
    def __init__(self, timestamp, contents, author):
        #turn time stamp into struct time tuple
        self.timestamp = time.strptime(timestamp, Message.date_format)
        #turn struct_time tuple into comparable number for easy comparison
        self.timestamp_cmp = time.mktime(self.timestamp)
        self.contents = contents
        self.author = author
        self.id = Message.id
        Message.id += 1
        # 0 for no, 1 for nickname, 2 for group name
        if Message.group_change_sig in self.contents:
            self.special = 2
        elif Message.name_change_sig in self.contents:
            self.special = 1
        else:
            self.special = 0
    def __str__(self):
        return "message #{}\nauthor: {}\nmessage: {}\ntime stamp: {}".format(
            self.id, self.author, self.contents, self.timestamp_cmp)
    def extract_name_change(self):
        if self.special == 0:
            return None
        elif self.special == 1:
            temp = self.contents.split(Message.name_change_sig)
            name, nickname = temp[1].split(" to ")
            nickname = nickname.rstrip(".")
        elif self.special == 2:
            temp = self.contents.split(Message.group_change_sig)
            nickname = temp[1].rstrip(".")
            name = "group"
        else:
            raise ValueError
        return (name, nickname)
#testcase 1

if __name__ == "__main__":
    test_arr = [
        ("Nov 29, 2017 9:19am",
         "Aanthruuk the scaly Scotsman set the nickname for Joseph G to Reverend Spicy-hands.",
         "Mike G",
         ("Joseph G", "Reverend Spicy-hands")
         )
    ]
    for i in test_arr:
        x = Message(i[0],i[1],i[2])
        print(x)
        print(x.extract_name_change())
        assert i[3] == x.extract_name_change()