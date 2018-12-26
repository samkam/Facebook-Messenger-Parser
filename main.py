# try to open zip file and read contents
import zipfile
from bs4 import BeautifulSoup

div_dic = {"_3-94":"date","_3-96 _2pio _2lek _2lel":"name"}
def open_zip(zipfilename,filename):
    with zipfile.ZipFile(zipfilename) as z:
        print(z.read(filename))

def main():
    text = ""
    with open("message.html",'rb') as f:
        text = f.read().decode('utf-8',"ignore")
        print(type(text))
    soup = BeautifulSoup(text)
    text = soup.get_text("\n").split("\n")
    with open("out.txt","w", encoding="utf-8") as f:
        for i in text:
            if "nickname" in i:
                f.write(i+"\n")


main()
