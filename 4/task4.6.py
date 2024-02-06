#!/usr/bin/env python3

#TASK46
ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
str_replace =ospf_route.replace(",", "")
tmp_ospf = str_replace.split(" ")

result = tmp_ospf[7:]
message = ('Prefix "{0}" \n'
          'AD/Metric  "{1}" \n'
          'Next-Hop "{2}" \n'
          'Last update "{3}" \n'
          'Outbound Interface"{4}" \n')
print(message.format(result[0],result[1],result[3],result[4],result[5]))