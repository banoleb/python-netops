import re


regex = r'(?P<mac>\S+) +(?P<ip>\S+) +\d+ +\S+ +(?P<vlan>\d+) +(?P<port>\S+)'
result_dict = []
with open('config_r1.txt') as data:
    for line in data:
        match = re.search('(?P<ip>\d+\.\d+\.\d+\.\d+)\s(?P<mac>\d+\.\d+\.\d+\.\d+)', line)
        if match != None:
            result_dict.append(match.groups())
print(result_dict)
