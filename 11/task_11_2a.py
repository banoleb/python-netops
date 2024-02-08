import os
from pprint import pprint
from draw_network_graph import draw_topology
cwd = os.getcwd() 

list_files = ["sh_cdp_n_sw1.txt","sh_cdp_n_r1.txt","sh_cdp_n_r2.txt","sh_cdp_n_r3.txt"]


def unique_check_map(topology_dict):
    check_map = {}
    for key, value in topology_dict.items():
        if not check_map.get(value) == key:
            check_map[key] = value
    return check_map


def create_check_map(filenames):
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
                
                if len(ii)>4:
                    if ii[3].isdigit():
                  
                        result[(router_name, ii[1]+ ii[2])] = (ii[0],ii[-2]+ ii[-1])
            main_list.clear()
    return result
if __name__ == "__main__":

    test= create_check_map(list_files)
    test2 = unique_check_map(test)
    draw_topology(test2)