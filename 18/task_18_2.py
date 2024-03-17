from netmiko import ConnectHandler
import yaml


commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]

def send_config_commands(device, config_commands):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        result = ssh.send_config_set(config_commands)
    return result


if __name__ == "__main__":

    #device = {
    #    "device_type": "cisco_ios",
    #    "host": "192.168.1.71",
    #    "username": "admin",
    #    "password": "cisco",
    #    "secret": "router1",
    #}
    with open("devices.yaml") as f:
        device = yaml.safe_load(f)
    for dev in device:
        print(send_config_commands(dev, commands))

