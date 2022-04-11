import os
import time 
from subprocess import *
import requests
import json

def options():
    osint()
    dos()

def osint():
    if user == '1':
        oslnt = input("ip or email: ")
        if oslnt == 'ip':
            clear()
            ip = input("ip of target:")
            iplook = requests.get('https://ipapi.co/'+ip+'/json/')
            print(iplook)

def dos():
    if user == '2':
        print("you have choosen dos")

def qr():
    if user == '3':
        print("you have choosen qr gen")
   
def clear():
    _ = call('clear' if os.name =='posix' else 'cls')

print("starting in 5..4..3..2..1") 
time.sleep(1)
clear()

print("________________")
print("|  (1) OSINT   |")
print("|              |")
print("|  (2) DOS     |")
print("|              |")
print("|  (3) QR      |")
print("|              |")
print("|              |")
print("|              |")
print("|              |")
print("|______________|")
print()
user = input("option: ")
clear()
options()

