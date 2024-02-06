#!/usr/bin/env python3


#TASK6.3

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk = {"0/1": ["add", "10", "20"], "0/2": ["only", "11", "30"], "0/4": ["del", "17"]}


for intf, vlan in trunk.items():
    for command in trunk_template:
        result_list=[]
        for i in vlan:
            result_list.append(i)
        if result_list[0]=="only":
            result_list.remove("only")
        elif result_list[0]=="del":
            result_list[0]="remove"
        if command.endswith("vlan"):
            print(f" {command} {' '.join(result_list)}")
        else:
            print(f" {command}")
