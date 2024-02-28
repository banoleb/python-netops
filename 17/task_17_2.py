# -*- coding: utf-8 -*-
import csv
import os
import re
from pprint import pprint
cwd = os.getcwd() 
import re
import glob


headers = ["hostname", "ios", "image", "uptime"]

def parse_sh_version(str_parse):
    my_tuple = ()
    reg = (
        "Cisco IOS Software, .*, Version (\S+), .*"
        "router uptime is (?P<uptime>[\S, ]*).*"
        """System image file is \"(\S+)\""""
    )
    match = re.search(reg, str_parse, re.DOTALL,)

    if match != None:
        my_tuple =  match.groups()
    print(my_tuple)
    return my_tuple


def write_inventory_to_csv(data_filenames, csv_filename):

    with open(csv_filename, "w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for filename in data_filenames:
            switch_name = re.search("sh_version_(\S+).txt", filename).group(1)
            with open(filename) as f:
                parsed_data = parse_sh_version(f.read())
                if parsed_data:
                    writer.writerow([switch_name] + list(parsed_data))

sh_version_files = glob.glob(cwd+"/python/python_for_netops/17/"+"sh_vers*")
write_inventory_to_csv(sh_version_files, "routers_inventory.csv")