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
    text = soup.get_text("\n").split("\n")
    '''
    divs = soup.select("._3-95._2pi0._2lej")
    for message in divs:
        name = message.find("._3-96._2pi0")
        txt = message.find("._3-96._2let")
    print(temp)
    print(type(divs[50]))

    message = ""
    name = ""
    date = ""
    print(len(divs))
    exit()
    #print(soup.prettify())
    text = soup.prettify()
    print(type(text))
    '''
    with open("out.html","w", encoding="utf-8") as f:
        for i in text:
            if "nickname" in i:
                f.write(i+"\n")


main()
