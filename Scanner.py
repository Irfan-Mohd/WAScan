from __future__ import print_function
from time import sleep
import readline
from Scan import Scan
from Header import Header
from Color import color


def process(url):
    header = Header(url)
    header.reader()
    print("Scanning: " + color.blue + url + color.end)
    if header.status:
        scanObj = Scan(url)
        scanObj._start()
    else:
        print(color.blue + url + color.red + " is Unreachable")
    sleep(3)

userInput = raw_input("File/URL: ")
if userInput == '':
    print(color.red + "Invalid Input" + color.end)

userInput = userInput.lower()
if 'f' == userInput[0] or '1' == userInput:
    userInput = raw_input("Enter File Name: ")
    try:
        urls = file(userInput, "r").readlines()
        for url in urls:
            process(url)
    except IOError:
        print("File Not Found, Operation Aborted.")
elif 'u' == userInput[0] or '2' == userInput:
    userInput = raw_input("Enter URL: ")
    if userInput == '':
        print("Invalid Input")
    else:
        process(userInput)
else:
    print("Invalid Input")
