import re


def parse_sh_ip_int_br(path):
    regex = r'(\S+)\s+(\d+.\d+.\d+.\d+)\s+\S+\s+\S+\s+(\S+)\s+(\S+)'
    result_dict = []
    with open(path) as data:
        dict_key_interface= ""
        dict_key_ipaddress= ""
        dict_key_status= ""
        dict_key_protocol= ""
        tuple_1 = ()
        for line in data:
            #print(line)
            if not line.startswith("Interface"):
                match = re.search(regex, line)
                if match != None:
                    dict_key_interface = match.group(1)    
                    dict_key_ipaddress= match.group(2)   
                    dict_key_status= match.group(3)   
                    dict_key_protocol= match.group(4)  
                    tuple_1=(dict_key_interface,dict_key_ipaddress,dict_key_status,dict_key_protocol)
                    result_dict.append(tuple_1)
    return result_dict


print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
