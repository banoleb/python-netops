#!/usr/bin/env python3
from sys import argv
import os

cwd = os.getcwd() 

ip_template = "{vlan:<8} {mac:<20} {inter:<20}"

#TASK7.3
list_main=[]
with open(cwd+'/python/CAM_table.txt', 'r') as conf:
    for line in conf:
        words = line.rstrip().split()
        
       
        if len(words)==4 and words[0].isdigit():
            print(ip_template.format(vlan=words[0],
                                    mac=words[1],
                                    inter=words[2])
                                    )

