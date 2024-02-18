import re

def get_ints_without_description(file_read):

    result_list = []
    with open(file_read) as data:
        regex = re.compile(r"^interface.(Tunnel\d|Loopback0|Ethernet\d\W\d|Ethernet\d\/\d+.\d+)\n(.description)?", re.MULTILINE)
        match = regex.finditer(data.read())
        for item in match:
            if list(item.groups())[1] ==None:
                result_list.append(list(item.groups())[0])
    return result_list

print(get_ints_without_description("config_r1.txt"))

#['Loopback0', 'Tunnel0', 'Ethernet0/1', 'Ethernet0/3.100', 'Ethernet1/0']