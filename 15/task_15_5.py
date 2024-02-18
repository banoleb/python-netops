import re
import os
from pprint import pprint
cwd = os.getcwd() 
def generate_description_from_cdp(file_read):
    result_dict = {}
    with open(cwd+"/python/python_for_netops/15/"+file_read) as f:
        for line in f:
            # print(line)
            regex = r"(^(?P<dev>\S+)\s+(?P<local>\S+.\d\/\d)\s+(\S+)\s+(\S....)\s+(\d+)\s+(?P<intf>\S+.\d\/\d))"
            match = re.search(regex,line)
            #"Eth 0/0": "description Connected to SW1 port Eth 0/1"
            if match != None:
                result_dict[match.group("local")] = "description Connected to " \
                + str(match.group("dev"))+ " port " + str(match.group("intf"))
    #print(result_dict)
    return result_dict
   

generate_description_from_cdp("sh_cdp_n_sw1.txt")