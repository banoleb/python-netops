from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import yaml
from netmiko import  ConnectHandler


def send_cfg_commands(device, commands):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(commands)
    return f"{result}\n"

def send_show_command(device, command):
    final=''
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        
        result = ssh.send_command(command)
        final += f"\n{result}\n"
    return final


def send_commands_to_devices(devices, filename, *, show=None, config=None, limit=3):
    if show and config:
        raise ValueError()
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_list = []
        for device in devices:
            if show:
                future = executor.submit(send_show_command, device, show)
            else:
                future = executor.submit(send_cfg_commands, device, config)
            print(device['host'])
            future_list.append(future)

        with open(filename, "w") as f:
            for fr in future_list:
                str = (fr.result())
                f.write(str)

with open('devices.yaml') as f:
    devices = yaml.safe_load(f)


send_commands_to_devices(devices, show="sh ip int br", filename="result_19_show.txt")
send_commands_to_devices(devices, config="logging 10.5.5.5", filename="result_19_conf.txt")