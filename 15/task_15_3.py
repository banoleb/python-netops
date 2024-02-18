import re


#ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022

#object network LOCAL_10.1.2.84
# host 10.1.2.84
# nat (inside,outside) static interface service tcp 22 20022


def convert_ios_nat_to_asa(file_read, file_write):
    result = {}
    list_temp =[]
    regex = r'(\S+)\s+(\d+.\d+.\d+.\d+)\s+(\S+)\s+\S+\s+\S+\s+(\S+)'
    with open(file_read) as f:
        for i in f.read().split("\n"):

            if i.startswith("ip"):
                match = re.search(regex, i)
                list_temp.append(match.group(1,2,3,4))
 

            ip_template = '''object network LOCAL_{net0}
 host {net1}
 nat (inside,outside) static interface service tcp {net2} {net3}'''        


            print(ip_template.format(net0=list_temp[0][1],
                                    net1=list_temp[0][1],
                                    net2=list_temp[0][2],
                                    net3=list_temp[0][3])
                                    )
            list_temp.clear()

convert_ios_nat_to_asa("cisco_nat_config.txt","cisco_nat_config_ASA.txt")


