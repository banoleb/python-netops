import os
from pprint import pprint
from draw_network_graph import draw_topology
import yaml
cwd = os.getcwd() 

list_configs=["sh_cdp_n_r1.txt","sh_cdp_n_r2.txt","sh_cdp_n_r3.txt","sh_cdp_n_r4.txt","sh_cdp_n_r5.txt","sh_cdp_n_r6.txt"]


def transform_topology(file_yml):
    with open(cwd+"/python/python_for_netops/17/"+file_yml) as f:
        templates = yaml.safe_load(f)
        final_dict ={}      
        for key,value in templates.items():
            r_int = list(value.items())
            for i in r_int:
                t_tmp1= (key, (i[0]))
                t_tmp2=(list((i[1].keys()))[0],  list((i[1].values()))[0])
                final_dict[t_tmp1]=t_tmp2
    return final_dict

    
def unique_check_map(topology_dict):
    check_map = {}
    for key, value in topology_dict.items():
        if not check_map.get(value) == key:
            check_map[key] = value
    return check_map

if __name__ == "__main__":

    
    pprint(unique_check_map(transform_topology("topology.yaml")))
    draw_topology(unique_check_map(transform_topology("topology.yaml")))