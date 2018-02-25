import urllib
def  read_file():
    profanity = open("C:\Python27\Projects\profanity.py")
    scan_content     = profanity.read()
    print(scan_content)
    profanity.close()
    profanity_check(scan_content)
    
def profanity_check(check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" +check)
    output   = connection.read()
    print(output)
    connection.close()
read_file()
