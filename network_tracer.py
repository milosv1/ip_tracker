#first commit of the project, essentially it will be a script or potentially a new side project - which tracks ip addresses, when a new -
#address connects it will send through an email or another form of notification to say that a new ip-addr. has made connection.
import sys
import subprocess
import os
import socket
import uuid
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-mi","--my_ip")
    parser.add_argument("-ma","--my_mac")
    args = parser.parse_args()
    if args.my_ip:
        print(f"{args.my_ip} works!")
        ip_ad = socket.gethostbyname(socket.gethostname())
        print("IP: ", ip_ad)
    elif args.my_mac:
          print("MAC address: ", end="")
          mac_add = print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
          for ele in range(0,8*6,8)][::-1])) 




get_args()
