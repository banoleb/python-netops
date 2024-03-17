import yaml
from pprint import pprint
from task_18_1 import send_show_command
from task_18_2 import send_config_commands


commands = ["logging 10.255.255.1", "logging buffered 20010", "no logging console"]
command = "sh ip int br"


def send_commands(device, *, config=None, show=None):
    if show and config:
        raise ValueError()
    elif show:
        return send_show_command(device, show)
    elif config:
        return send_config_commands(device, config)


if __name__ == "__main__":

    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)[0]
    print(send_commands(devices, config=commands))
    print(send_commands(devices, show=command))