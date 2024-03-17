from pprint import pprint
import yaml
from netmiko import (
    ConnectHandler,
    NetmikoAuthenticationException,
)



def send_show_command(device, command):
    #result = {}
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()

            output = ssh.send_command(command)
            result = output
        return result
    except (NetmikoAuthenticationException) as error:
        print(error)

if __name__ == "__main__":
    command = "sh ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)

    for dev in devices:
        print(send_show_command(dev, command))