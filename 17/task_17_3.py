# -*- coding: utf-8 -*-
import os
from pprint import pprint
cwd = os.getcwd() 



def parse_sh_cdp_neighbors(command_output):
    main_list = []
    result = {}
    to_j2={}
    to_json = {}
    for i in command_output.split("\n"):
        if ">" in i:
            sw_1 = i.split(">")[0]
        if (i != ""):
            main_list.append(i.split())
    for ii in main_list:
        if len(ii)>4:
            if ii[3].isdigit():
                result={}
                result[ii[0]]=str(ii[-2]+" " +ii[-1])
                to_json[(ii[1]+" " +ii[2])] = result
                to_j2[sw_1]=to_json
          
    return to_j2
if __name__ == "__main__":
    with open(cwd+"/python/python_for_netops/17/sh_cdp_n_sw1.txt") as f:
        pprint(parse_cdp_neighbors(f.read()))


