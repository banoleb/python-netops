import yaml
import sqlite3
import csv
import os
import re
from pprint import pprint
cwd = os.getcwd() 
import re


list_configs=["switches.yml"]
list_conf_dhcp=["sw1_dhcp_snooping.txt","sw2_dhcp_snooping.txt","sw3_dhcp_snooping.txt"]

def get_yml_sw():
    # Чтение данных из YAML файла
    with open(list_configs[0], 'r') as f:
        data = yaml.safe_load(f)

    # Преобразование данных в список с кортежами
    for key,value in data.items():
        r_int = list(value.items())
    return r_int


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
         
       

getyml=get_yml_sw()
data= get_dhcp_snooping(list_conf_dhcp)

connection = sqlite3.connect('dhcp_snooping.db')
cursor = connection.cursor()
query = "REPLACE into switches values (?, ?)"
print("Добавляю данные в таблицу switches...")
for row in getyml:
    print("При добавлении данных:", row)
    cursor.execute(query, row)

query2 = "replace into dhcp values (?, ?, ?, ?, ?, ?, datetime('now'))"
print("Добавляю данные в таблицу dhcp...")
for row in data:
    cursor.execute(query2, row)
    print("При добавлении данных:", row)
connection.commit()
connection.close()