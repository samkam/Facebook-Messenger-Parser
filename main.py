# try to open zip file and read contents
import zipfile
import re
from bs4 import BeautifulSoup
import message_repackage
div_dic = {"_3-94":"date","_3-96 _2pio _2lek _2lel":"name"}
def open_zip(zipfilename,filename):
    with zipfile.ZipFile(zipfilename) as z:
        print(z.read(filename))

def extract_text():
    text = ""
    with open("message.html",'rb') as f:
        text = f.read().decode('utf-8',"ignore")
        print(type(text))
    soup = BeautifulSoup(text)
    text = soup.get_text("\n").split("\n")
    with open("out.txt","w", encoding="utf-8") as f:
        for i in text:
            f.write(i + "\n")
            '''
            if "nickname" in i:
                f.write(i+"\n")
            '''
if __name__ == "__main__":
    lines = []
    with open("out.txt",'rb') as f:
        lines =[x.decode('utf-8','ignore') for x in f.readlines()]
    # skip to line past "participants"
    index = 0
    while "partcipants" not in temp:
        temp = lines[index]
        index+=1
    messages = []
    temp_date_line = ""
    temp_author_line = ""
    temp_message = ""
    stage = 0
    for i in range(index, len(lines)):
        x = "^\w{3}\s*\d{1,2},\s*\d{4}\s*\d\:\d{2}.m"
        if re.match(x, lines[i]):
            temp = message_repackage.Message(temp_date_line,
                                             temp_message,
                                             temp_author_line)
            temp_date_line = lines[i]
            temp_author_line = ""
            temp_message = ""
            messages.append(temp)
            stage = 1
        elif stage == 1:
            temp_author_line = lines[i]
            stage +=1
        elif stage == 2:
            temp_message += "\n" +lines[i]
        else:
            print("something has gone wrong")


    # need to make its own class, converting from log to messages
    # messages delimited by
    #happy case, message one line long,

    '''
    divide by lines that can be interpreted as a date
    1st line is time stamp,
    next line is author
    the rest is message
    '''
    timestamp = f.readline().decode('utf-8','ignore')
    author = f.readline().decode('utf-8','ignore')
    message = f.readline().decode('utf-8','ignore')
    x = message_repackage.Message(timestamp, message, author)
    print(x)
    print(x.extract_name_change())

