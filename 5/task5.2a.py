#!/usr/bin/env python3
#TASK5.2a_Lvov


get_inpute = input('ввод IP-сети в формате: 10.1.1.0/24: ')
all_list = get_inpute.split("/") 

ip_list = all_list[0].split(".")
net_list = all_list[1]


print(ip_list)
print(net_list)


mask_math= "1" * int(net_list) + "0" * (32 - int(net_list))
mask_all = [mask_math[0:8],mask_math[8:16],mask_math[16:24],mask_math[24:32]]



ip_math1 =  bin(int(ip_list[0]))[2:]
ip_math1_all = "00000000" + str(ip_math1)
ip_math1_all = ip_math1_all[-8:]

ip_math2 =  bin(int(ip_list[1]))[2:]
ip_math2_all = "00000000" + str(ip_math2)
ip_math2_all = ip_math2_all[-8:]

ip_math3 =  bin(int(ip_list[2]))[2:]
ip_math3_all = "00000000" + str(ip_math3)
ip_math3_all = ip_math3_all[-8:]

ip_math4 =  bin(int(ip_list[3]))[2:]
ip_math4_all = "00000000" + str(ip_math4)
ip_math4_all = ip_math4_all[-8:]


all = (str(ip_math1_all) + str(ip_math2_all) + str(ip_math3_all) + str(ip_math4_all))
all_net = all[:int(net_list)]  + "0" * (32 - int(net_list))
net_l = [all_net[0:8],all_net[8:16],all_net[16:24],all_net[24:32]]
print(net_l)




ip_template = '''
Network:
{net0:<8} {net1:<8} {net2:<8} {net3:<8}
{net0:08b} {net1:08b} {net2:08b} {net3:08b}

Mask:*/{mask_human}
{mask0:<8} {mask1:<8} {mask2:<8} {mask3:<8}
{mask0:08b} {mask1:08b} {mask2:08b} {mask3:08b}
'''


print(ip_template.format(net0=int(net_l[0],2),
                         net1=int(net_l[1],2),
                         net2=int(net_l[2],2),
                         net3=int(net_l[3],2),
                         mask_human=int(net_list),
                         mask0=int(mask_all[0],2),
                         mask1=int(mask_all[1],2),
                         mask2=int(mask_all[2],2),
                         mask3=int(mask_all[3],2))
                         )


