#!/usr/bin/env python3
from sys import argv
import os

cwd = os.getcwd() 

ip_template = "{vlan:<8} {mac:<20} {inter:<20}"

#TASK7.3
list_main=[]
temp=[]
with open(cwd+'/python/CAM_table.txt', 'r') as conf:
    ii=0
    for line in conf:
        words = line.rstrip().split()
       
        if len(words)==4 and words[0].isdigit():
            temp=[int(words[0]),words[1],words[2]]
            list_main.append(temp)
            list_main.sort()

    ii=ii+1
    for i in list_main:

        print(ip_template.format(vlan=i[0],
                                mac=i[1],
                                inter=i[2])
                                )
