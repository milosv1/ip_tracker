#first commit of the project, essentially it will be a script or potentially a new side project - which tracks ip addresses, when a new -
#address connects it will send through an email or another form of notification to say that a new ip-addr. has made connection.
import sys
import subprocess
import os
import socket
import uuid
import argparse
from datetime import date
import calendar as c
from time import gmtime, strftime

t = date.today()
m_d = date.today()
day = c.day_name[m_d.weekday()]
t_n = strftime("%H:%M:%S",gmtime())

def time_now():
    t_now = t.strftime(f"{day} %B %d")
    print("Last login: ", t_now, t_n)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-mi","--my_ip")
    parser.add_argument("-ma","--my_mac")
    args = parser.parse_args()
    if args.my_ip:
        ip_ad = socket.gethostbyname(socket.gethostname())
        print("IP: ", ip_ad)
    elif args.my_mac:
          print("MAC address: ", end="")
          mac_add = print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
          for ele in range(0,8*6,8)][::-1])) 




time_now()
get_args()
