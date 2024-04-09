from netmiko.cisco.cisco_ios import CiscoIosSSH
from netmiko import ConnectHandler
import re


class ErrorInCommand(Exception):
    """
    Исключение генерируется, если при выполнении команды на оборудовании, возникла ошибка.
    """


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

    def _check_error_in_command(self, command, result):
        regex = "% (?P<err>.+)"
        error = ('При выполнении команды "{}" на устройстве {} возникла ошибка "{}"')
        error_command = re.search(regex, result)
        if error_command==True:
            raise ErrorInCommand(
                error.format(command,self.host,error_command.group("err"))
            )

    def send_config_set(self, command, ignore_errors=True, *args, **kwargs):
        if ignore_errors:
            result = super().send_config_set(command, *args, **kwargs)
            return result
        with ConnectHandler(**device_params) as net_connect:
            net_connect.enable()
            result = net_connect.send_command(command)

            self._check_error_in_command(command, result)
            return result

device_params = {
        "device_type": "cisco_ios",
        "ip": "192.168.1.85",
        "username": "admin",
        "password": "cisco",
        "secret": "router1",
}


r1 = MyNetmiko(**device_params)
print(r1.send_config_set('lo', ignore_errors=False, st_command=False))
