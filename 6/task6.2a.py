#!/usr/bin/env python3


#TASK6.2a
ip_input = input("введите ip-адрес: ")
list_ip = ip_input.split(".")
result = True
if len(list_ip) == 4:
    for i in list_ip:
        if  not (i.isdigit() and 0 <= int(i) <= 255):
            print("Неправильный IP-адрес")
            result = False
            break
    if result:
        first_item = int(list_ip[0])
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