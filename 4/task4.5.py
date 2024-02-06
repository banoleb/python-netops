#!/usr/bin/env python3

#TASK45

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
tmp1= command1.split()
tmp2= command2.split()
tmp1 = set(tmp1[-1].split(","))
tmp2 = set(tmp2[-1].split(","))

print(tmp1.intersection(tmp2))