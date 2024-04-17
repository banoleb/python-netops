import sqlite3
import os
import re
from pprint import pprint
cwd = os.getcwd() 
import re

list_conf_dhcp=["sw1_dhcp_snooping.txt","sw2_dhcp_snooping.txt","sw3_dhcp_snooping.txt"]
connection = sqlite3.connect('dhcp_snooping.db')
cursor = connection.cursor()

#def checkitem(mac):
#    print(mac)
#    counter  = cursor.execute('select * from dhcp where mac = '+"'"+str(mac)+"'")
#    print(counter)


def get_dhcp_snooping(filenames):
    result_dict = []
    for count,items_files in enumerate(filenames):
        with open(cwd+"/new_data/"+items_files) as f:
            match = re.search('(\S+?)_\S+', items_files)
            if match != None:
                switch_name = match.group(1)
            regex =  r'^(\S+)\s+(\S+)\s+(\d+)\s+(\S+)\s+(\d+)\s+(\S+)$'

            for line in f:
                match = re.search(regex, line)
                if match:
                    mac_address = match.group(1)
                    ip_address = match.group(2)
                    vlan = match.group(3)
                    interface = match.group(6)
                    status= 1
                    r_int = (mac_address,ip_address,vlan,interface,switch_name,status)
                    result_dict.append(r_int)

    return result_dict
  

data= get_dhcp_snooping(list_conf_dhcp)
query2 = "REPLACE into dhcp values (?, ?,?,?,?,?)" 
print("Добавляю данные в таблицу dhcp...")
cursor.execute("update dhcp set active = 0")
for row in data:
    cursor.execute(query2, row)
    print("При добавлении данных:", row)
connection.commit()


cursor.execute('select * from dhcp')
pprint(cursor.fetchall())

connection.close()