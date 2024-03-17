from netmiko import ConnectHandler
import yaml
import re
from pprint import pprint

commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

def send_config_commands(device, config_commands,log=True):
    regex = "%\s(.+)"
    good_commands = {}
    bad_commands = {}
    if log:
        print(f"Подключаюсь к {device['host']}...")
    with ConnectHandler(**device) as ssh:
       
        for item in config_commands:
                
           # result = ssh.send_config_set(config_commands)
            ssh.enable()
            result = ssh.send_config_set(item, exit_config_mode=False)

            error_in_result = re.search(regex, result)
            if error_in_result:
                print(
                f"Команда {item} выполнилась с ошибкой "
                f"{error_in_result.group(1)} на устройстве "
                f"{device['host']}"
                )
                bad_commands[item] = error_in_result.group(1)
            else:
                good_commands[item] = result
        ssh.exit_config_mode()
    return good_commands, bad_commands


if __name__ == "__main__":

    with open("devices.yaml") as f:
        device = yaml.safe_load(f)
    for dev in device:
        pprint(send_config_commands(dev, commands))

