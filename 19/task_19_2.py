from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import yaml
from netmiko import  ConnectHandler

def send_show_command(device, command):
    #result = {}

    with ConnectHandler(**device) as ssh:
        ssh.enable()

        output = ssh.send_command(command)
        result = output
    return result


with open('devices.yaml') as f:
    devices = yaml.safe_load(f)

with ThreadPoolExecutor(max_workers=3) as executor:
    future_list = []
    for device in devices:
        command = "sh ip int br"
        future = executor.submit(send_show_command, device, command)
        print(device['host'])
        future_list.append(future)

    with open('save_19_2.log', "w") as f:
        for fr in future_list:
            str = (fr.result())
            f.write(str)