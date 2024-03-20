import textfsm
from netmiko import  ConnectHandler
from pprint import pprint



def parse_output_to_dict(template, command_output):
    with open(template) as base:
        parser = textfsm.TextFSM(base)
        header = parser.header
        result = parser.ParseText(command_output)
        resultt=[]
        for i in result:
            resultt.append(dict(zip(header, i)))
    return resultt


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
    result = parse_output_to_dict("templates/sh_ip_int_br.template", output)
    pprint(result)   
