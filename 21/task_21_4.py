import os
from pprint import pprint
from netmiko import ConnectHandler
import yaml


def send_and_parse_show_command(device_dict, command, templates_path):
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command, use_textfsm=True)
    return output



with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
for i in devices:
    result = send_and_parse_show_command(i, "sh ip int br", "templates")
   # pprint(result, width=120)
