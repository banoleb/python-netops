#!/usr/bin/env python3


#TASK6.2a

while True:
    ip_input = input("введите ip-адрес: ")
    list_ip = ip_input.split(".")
    print(list_ip)
    result = True
    if len(list_ip) == 4:
        for i in list_ip:
            if  (i.isdigit() and 0 <= int(i) <= 255):
                result = False
            else:
                print("Неправильный IP-адрес")
                result = True
    else:
        result = False
        print("Неправильный IP-адрес")
    if result==False:
        break




if result==False:
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