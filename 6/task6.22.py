#!/usr/bin/env python3


#TASK6.2
ip_input = input("введите ip-адрес: ")
first_item = int(ip_input.split(".")[0])
if ip_input == "255.255.255.255":
    print("local broadcast")
elif ip_input == "0.0.0.0":
    print("unassigned")
elif 1 <= first_item <= 223:
    print("unicast")
elif 224 <= first_item <= 239:
    print("multicast")
else:
    print("unused")