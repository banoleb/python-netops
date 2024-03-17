from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import yaml
from netmiko import  ConnectHandler

# Этот словарь нужен только для проверки работа кода, в нем можно менять IP-адреса
# тест берет адреса из файла devices.yaml
commands = {
    "192.168.1.71": "sh run | s ^router ospf",
    "192.168.1.72": "sh ip int br",
    "192.168.1.74": "sh int desc",
}


def send_show_command(device, command):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return f"{command}\n{result}\n"


with open('devices.yaml') as f:
    devices = yaml.safe_load(f)

with ThreadPoolExecutor(max_workers=3) as executor:
    future_list = []
    for device in devices:
        command = commands[device['host']]
        future = executor.submit(send_show_command, device, command)
        print(device['host'])
        future_list.append(future)

    with open('save_19_3.log', "w") as f:
        for fr in future_list:
            str = (fr.result())
            f.write(str)