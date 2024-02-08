import os
from pprint import pprint

cwd = os.getcwd() 

list_files = ["sh_cdp_n_sw1.txt","sh_cdp_n_r1.txt","sh_cdp_n_r2.txt","sh_cdp_n_r3.txt"]


def create_network_map(filenames):
    main_list = []
    result = {}
    for items_files in filenames:    
        with open(cwd+"/python/11/"+items_files) as f:
            router_name=""
            for i in f.read().split("\n"):
                if ">" in i:
                    router_name = i.split(">")[0]      
                    continue
                if (i != ""):
                    main_list.append(i.split())     
            for ii in main_list: 
                if len(ii)>4 and ii[3].isdigit():
                        result[(router_name, ii[1]+ ii[2])] = (ii[0],ii[-2]+ ii[-1])
            main_list.clear()
    return result
if __name__ == "__main__":
    pprint(create_network_map(list_files))