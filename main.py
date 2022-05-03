import os
import time 
from subprocess import *
import socket
import requests
import json
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from scapy.all import *

def options():
    osint()
    dos()

def osint():
    if user == '1':
        oslnt = input("ip or phone: ")
        if oslnt == 'ip':
            clear()
            ip = input("ip of target: ")
            iplook = requests.get('https://ipapi.co/'+ip+'/json/')
            print(iplook.content)
        if oslnt == 'phone':
            clear()
            phoneNumber = input("Enter phone number with country code(+1): ")
            phoneNumber = phonenumbers.parse(phoneNumber)
            print("Timezone:",timezone.time_zones_for_number(phoneNumber))
            print("Carrier:",carrier.name_for_number(phoneNumber, "en"))  
            print("Location:",geocoder.description_for_number(phoneNumber, "en"))

def dos():
    if user == '2':
        print("you have choosen dos")

def portscan():
    if user == '3':
        print("You have choosen port scanner")
   
def clear():
    _ = call('clear' if os.name =='posix' else 'cls')

print("starting in 5..4..3..2..1") 
time.sleep(1)
clear()

print("___________________")
print("|                 |")
print("|  (1) OSINT      |")
print("|                 |")
print("|  (2) DOS        |")
print("|                 |")
print("|  (3) Port Scan  |")
print("|_________________|")
print()
user = input("option: ")
clear()
options()
