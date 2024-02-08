from pprint import pprint
import sys
import subprocess
sys.path.append("..")
import ipaddress
from tabulate import tabulate


good_ip = ["10.1.1.1", "10.1.1.2"]
bad_ip = ["10.1.1.7", "10.1.1.8", "10.1.1.9"]

def print_ip_table(good_ip, bad_ip):
    table = {"Reachable": good_ip, "Unreachable": bad_ip}
    print(tabulate(table, headers=table.keys()))

print_ip_table(good_ip, bad_ip)