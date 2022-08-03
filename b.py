#! /usr/bin/python3
import webbrowser, sys

if len(sys.argv) < 3:
    print("Usage: openinbrowser.py ./urls.txt 20")
    quit()

f = open(sys.argv[1])
tabs = int(sys.argv[2])
counter = 1

for url in f:
    print(url)
    counter += 1
    webbrowser.open(url)
    if counter == tabs:
        input("Press any key to continue...")
        counter = 1  
