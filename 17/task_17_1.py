# -*- coding: utf-8 -*-
import csv
import os
import re
from pprint import pprint
cwd = os.getcwd() 
import re

list_files = ["sw1_dhcp_snooping.txt","sw2_dhcp_snooping.txt","sw3_dhcp_snooping.txt"]

def write_dhcp_snooping_to_csv(filenames,output):
    list_result = []
    for count,items_files in enumerate(filenames):
        with open(cwd+"/python/python_for_netops/17/"+items_files) as f:
            match = re.search('(\S+?)_\S+', items_files)
            if match != None:
                switch_name = match.group(1)
            reader = csv.reader(f, delimiter=' ')
            for row in reader:
                if row[0].strip() =="------------------" or row[0].strip() == "Total":             
                    continue
                else:
                    while("" in row):
                        row.remove("")
                    if row[0].strip() =="MacAddress" and count==0:
                        row.insert(0,"switch")
                    elif row[0].strip() =="MacAddress":
                        continue
                    else:
                        row.insert(0,switch_name)
                list_result.append(row)
           
        with open(cwd+"/python/python_for_netops/17/"+output, 'w') as ff:
            writer = csv.writer(ff)
            for roww in list_result:
                writer.writerow(roww)

        
if __name__ == "__main__":
    pprint(write_dhcp_snooping_to_csv(list_files,"tast_17_1_output.txt"))