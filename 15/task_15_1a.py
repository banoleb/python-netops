import re

# ip address 10.1.1.1 255.255.255.255


def get_ip_from_cfg(path):
    regex = r'(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<port>\S+)'
    result_dict = {}
    with open('python/python_for_netops/14/'+path) as data:
        dict_key= ""
        dict_value=""
        for line in data:

            if line.startswith("interface"):
                match = re.search('interface.(Tunnel\d|Loopback0|Ethernet\d\W\d)', line, re.DOTALL)
                if match != None:
                    dict_key = match.group(1)
                    #print(match.group(1))
                else:
                    continue    
            elif line.startswith(" ip address"):
                match = re.search('ip.address.(?P<ip>\d+\.\d+\.\d+\.\d+)\s(?P<mac>\d+\.\d+\.\d+\.\d+)', line, re.DOTALL)
                dict_value = match.groups()
                if match != None and dict_key!="":
                    result_dict[dict_key]=dict_value
    #print(result_dict)
    return result_dict

get_ip_from_cfg('config_r1.txt')
#(^interface)+\s.+().(\s.+)+(\s+) ip.address.(?P<ip>\d+\.\d+\.\d+\.\d+)\s(?P<mac>\d+\.\d+\.\d+\.\d+)


#interface.(Tunnel\d|Loopback0|Ethernet\d\W\d&|Ethernet\d\W\d.\d+)