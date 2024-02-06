#!/usr/bin/env python3
from sys import argv
import os

cwd = os.getcwd() 




file = argv[1]

#TASK7.2
result = {}

with open(cwd+'/python/'+file, 'r') as f:
    #for line in f:
    #    line_list = line.split()
    #    result_string = ', '.join(line_list)
    #    if result_string =="!":
    #        continue
    #    print(result_string)
    for line in f:
        if not line.startswith("!"):
            print(line.rstrip())