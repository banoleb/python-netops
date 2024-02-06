#!/usr/bin/env python3


#TASK5.2


get_inpute = input('ввод IP-сети в формате: 10.1.1.0/24: ')
all_list = get_inpute.split("/") 

ip_list = all_list[0].split(".")
mask_list = all_list[1]


mask_math= "1" * int(mask_list) + "0" * (32 - int(mask_list))


mask01 = mask_math[0:8]
mask02 = mask_math[8:16]
mask03 = mask_math[16:24]
mask04 = mask_math[24:32]

mask_l = [mask01,mask02,mask03,mask04]

ip_template = '''
IP address:
{ip0:<8} {ip1:<8} {ip2:<8} {ip3:<8}
{ip0:08b} {ip1:08b} {ip2:08b} {ip3:08b}
Mask:
{mask0:<8} {mask1:<8} {mask2:<8} {mask3:<8}
{mask0:08b} {mask1:08b} {mask2:08b} {mask3:08b}
'''


print(ip_template.format(ip0=int(ip_list[0]),
                         ip1 = int(ip_list[1]),
                         ip2= int(ip_list[2]),
                         ip3= int(ip_list[3]),
                         mask0=int(mask_l[0],2),
                         mask1=int(mask_l[1],2),
                         mask2=int(mask_l[2],2),
                         mask3=int(mask_l[3],2))
                         )