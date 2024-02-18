import re

def get_ip_from_cfg(path):

    result_dict = {}
    with open(path) as data:
        dict_key= ""
        dict_value=""
        dict_value_ips=[]
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
                    dict_value_ips.append(dict_value)
                    result_dict[dict_key]=dict_value_ips.copy()
            else:
                dict_value_ips.clear()
    return result_dict

get_ip_from_cfg('config_r2.txt')
