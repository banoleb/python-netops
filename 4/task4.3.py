#!/usr/bin/env python3

#TASK43
config = "switchport trunk allowed vlan 1,3,10,20,30,100"
temp_list = config.split()
result= temp_list[-1].split(",")

print(result)