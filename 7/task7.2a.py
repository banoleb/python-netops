#!/usr/bin/env python3
from sys import argv
import os

cwd = os.getcwd() 


file = argv[1]

#TASK7.2
result = {}
ignore = ["duplex", "alias", "configuration"]
with open(cwd+'/python/'+file, 'r') as f:
    for line in f:
        if not line.startswith("!"):
            find =0
            for i in ignore:
                if i  in line :
                    find =1
                    break
            if find ==0:
                print(line.rstrip())
