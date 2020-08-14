#first commit of the project, essentially it will be a script or potentially a new side project - which tracks ip addresses, when a new -
#address connects it will send through an email or another form of notification to say that a new ip-addr. has made connection.
import sys
import subprocess
import os
import socket
import uuid


def get_mac():  
    print("MAC address: ", end="")
    mac_add = print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
    for ele in range(0,8*6,8)][::-1])) 


def get_ip():
    ip_ad = socket.gethostbyname(socket.gethostname())
    print("IP: ", ip_ad)



get_mac()
get_ip()
