#!/usr/bin/env python3
from sys import argv
import os

cwd = os.getcwd() 


file = argv[1]
file2 = argv[2]
#TASK7.2
result = {}
ignore = ["duplex", "alias", "configuration"]
with open(cwd+'/python/'+file, 'r') as f, open(cwd+'/python/'+file2, 'w') as dest:
    for line in f:
        if not line.startswith("!"):
            find =0
            for i in ignore:
                if i  in line :
                    find =1
                    break
            if find ==0:
                print(line.rstrip())
                dest.writelines(line.rstrip()+'\n')
