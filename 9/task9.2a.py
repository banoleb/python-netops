#!/usr/bin/env python3
from pprint import pprint

#TASK9.2

trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

def generate_trunk_config(t_config, t_template):

    result = []
    finalresult={}
    for i,y in t_config.items():
        #
        result.append("interface "+i)
        result.append(t_template[0])
        result.append(t_template[1])
        result.append(t_template[2]+" "+(" ".join(str(x) for x in y)))
        finalresult[i]=result
        result = []


    return finalresult


pprint(generate_trunk_config(trunk_config,trunk_mode_template))


