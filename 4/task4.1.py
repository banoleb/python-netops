#!/usr/bin/env python3

#TASK41
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat.replace('FastEthernet', 'GigabitEthernet'))
#ip nat inside source list ACL interface GigabitEthernet0/1 overload