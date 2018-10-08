# try to open zip file and read contents
import zipfile


def open_zip(zipfilename,filename):
    with zipfile.ZipFile(zipfilename) as z:
        print(z.read(filename))


def main():
    open_zip("test.zip","test2/test3.txt")


main()
