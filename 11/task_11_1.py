import os
from pprint import pprint

cwd = os.getcwd() 

def parse_cdp_neighbors(command_output):
    main_list = []
    result = {}
    for i in command_output.split("\n"):
        if ">" in i:
            sw_1 = i.split(">")[0]
        if (i != ""):
            main_list.append(i.split())
    for ii in main_list:
        if len(ii)>4:
            if ii[3].isdigit():
                result[(sw_1, ii[1]+ ii[2])] = (ii[0],ii[-2]+ ii[-1])
    return result
if __name__ == "__main__":
    with open(cwd+"/python/11/sh_cdp_n_sw1.txt") as f:
        pprint(parse_cdp_neighbors(f.read()))