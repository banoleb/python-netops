#!/usr/bin/env python3


#TASK9.1a

access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]
port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]
access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}

def generate_access_config(intf_vlan_mapping, access_template,psecurity=None):

    result = []
    templist = list(intf_vlan_mapping.keys())
    tempvaluses = list(intf_vlan_mapping.values())

    ii=0
    for i in templist:

        result.append("interface "+i)
        result.append(access_template[0])
        result.append(access_template[1]+" " +str(tempvaluses[ii]))
        result.append(access_template[2])
        result.append(access_template[3])
        result.append(access_template[4])
        if psecurity != None:
            result.append(psecurity[0])
            result.append(psecurity[1])
            result.append(psecurity[2])
        ii = ii+1

    return result


print(generate_access_config(access_config,access_mode_template))


print(generate_access_config(access_config, access_mode_template, port_security_template))