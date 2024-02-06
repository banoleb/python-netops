#!/usr/bin/env python3


#TASK5.3
trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]
access_template = [
    "switchport mode access", "switchport access vlan {}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]


dict_comand= {"trunk": trunk_template, "access": access_template}




net_param1 = input('Введите режим работы интерфейса (access/trunk):')
net_tmp_check = dict_comand.get(net_param1, "Такого параметра нет - error - exit")
net_param2 = input('Введите тип и номер интерфейса: ')
net_param3 = input('Введите номер влан(ов): ')


print(f"interface {net_param2}")
print("\n".join(dict_comand[net_param1]).format(net_param3))

