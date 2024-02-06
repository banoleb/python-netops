#!/usr/bin/env python3


#TASK5.3a
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
dict_ask = {"trunk": "Введите разрешенные VLANы: ", "access": "Введите номер VLAN: "}



net_param1 = input('Введите режим работы интерфейса (access/trunk):')
net_tmp_check = dict_comand.get(net_param1, "Такого параметра нет - error - exit")
net_param2 = input('Введите тип и номер интерфейса: ')
net_param3 = input(dict_ask[net_param1])


print(f"interface {net_param2}")
print("\n".join(dict_comand[net_param1]).format(net_param3))

