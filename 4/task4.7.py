#!/usr/bin/env python3

#TASK47
mac = "AAAA:BBBB:CCCC"
temp_mac = mac.split(":")
result_mac = format(int(temp_mac[0],16),"b") + "" +format(int(temp_mac[1],16),"b")+ "" +format(int(temp_mac[2],16),"b")
print(str(result_mac))