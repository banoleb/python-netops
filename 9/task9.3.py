#!/usr/bin/env python3
from pprint import pprint
from sys import argv
import os

cwd = os.getcwd() 


file = argv[1]

#TASK9.3

def get_int_vlan_map():
    with open(cwd+'/python/9/'+file, 'r') as f:
        result_access = {}
        result_trunk = {}
        result = {}
        key_tmp = ""
        for line in f:
            if not line.startswith("!"):
                pass
            if line.startswith("interface Fast"):
                 key_tmp=line.rstrip()
                 result[key_tmp] = ""
            if line.startswith(" switchport trunk allowed vlan"):
                    result[key_tmp] = line.rstrip()[31:].split(",")
                    
            elif line.startswith(" switchport access vlan"):
                    result[key_tmp] = line.rstrip()[24:]
            elif line.startswith(" duplex auto") and result[key_tmp]=="":
                 del result[key_tmp]
    for i,ii in result.items():
        if (isinstance(ii, str)):
            result_access[i]=ii
        else:
            result_trunk[i]=ii 
         #   result_access 
    return result_access,result_trunk




pprint(get_int_vlan_map())



