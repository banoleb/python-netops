import yaml
from task_17_3 import parse_sh_cdp_neighbors
import os
from pprint import pprint

cwd = os.getcwd() 

list_configs=["sh_cdp_n_r1.txt","sh_cdp_n_r2.txt","sh_cdp_n_r3.txt","sh_cdp_n_r4.txt","sh_cdp_n_r5.txt","sh_cdp_n_r6.txt","sh_cdp_n_sw1.txt"]

def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    topology = {}
    for filename in list_of_files:
        with open(cwd+"/python/python_for_netops/17/"+filename) as f:
            topology.update(parse_sh_cdp_neighbors(f.read()))
    if save_to_filename != None:
        with open(save_to_filename, "w") as ff:
            yaml.dump(topology, ff)
    return topology


if __name__ == "__main__":
    pprint(generate_topology_from_cdp(list_configs, save_to_filename=(cwd+"/python/python_for_netops/17/topology.yaml")))