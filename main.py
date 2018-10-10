# try to open zip file and read contents
import zipfile
from bs4 import BeautifulSoup

div_dic = {"_3-94":"date","_3-96 _2pio _2lek _2lel":"name"}
def open_zip(zipfilename,filename):
    with zipfile.ZipFile(zipfilename) as z:
        print(z.read(filename))


def main():
    #open_zip("D:/facebook.zip","messages/TheJuggleBoys_c1a61d1fa1/message.html")
    text = ""

    with open("message.html",'rb') as f:
        text = f.read().decode('utf-8',"ignore")
        print(type(text))
    soup = BeautifulSoup(text)
    #print(soup.prettify())
    text = soup.prettify()
    print(type(text))
    with open("out.html","w", encoding="utf-8") as f:
        f.write(text)


main()
