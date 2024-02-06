#!/usr/bin/env python3


#TASK5.1b-5.1d
london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1"
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2"
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True
    }
}

net_name = input('Введите имя устройства: ')
print(london_co[net_name].keys())

net_param = input('Введите имя параметра: ').lower()
net_tmp = london_co[net_name].get(net_param, "Такого параметра нет")

print(net_tmp)