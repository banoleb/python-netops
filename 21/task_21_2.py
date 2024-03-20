from netmiko import  ConnectHandler
from pprint import pprint
from task_21_1 import parse_command_output


# вызов функции должен выглядеть так
if __name__ == "__main__":
    r1_params = {
        "device_type": "cisco_ios",
        "host": "192.168.1.73",
        "username": "admin",
        "password": "cisco",
        "secret": "router1",
    }
   # with ConnectHandler(**r1_params) as r1:
   #     r1.enable()
    #    output = r1.send_command("sh_ip_dhcp_snooping")
    with open("output/sh_ip_dhcp_snooping.txt") as show:
        output = show.read()
    result = parse_command_output("templates/sh_ip_dhcp_snooping.template", output)
    pprint(result)   
