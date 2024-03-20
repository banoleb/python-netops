import textfsm
from netmiko import  ConnectHandler

def parse_command_output(template, command_output):
    with open(template) as base:
        parser = textfsm.TextFSM(base)
        li =[]
        li.append(parser.header)
        result = parser.ParseText(command_output)
    return li + result





# вызов функции должен выглядеть так
if __name__ == "__main__":
    r1_params = {
        "device_type": "cisco_ios",
        "host": "192.168.1.73",
        "username": "admin",
        "password": "cisco",
        "secret": "router1",
    }
    with ConnectHandler(**r1_params) as r1:
        r1.enable()
        output = r1.send_command("sh ip int br")
    result = parse_command_output("templates/sh_ip_int_br.template", output)
    print(result)   
