from base_connect_class import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.ssh.enable()

device_params = {
       "device_type": "cisco_ios",
        "ip": "192.168.1.85",
        "username": "admin",
        "password": "qwerty",
        "secret": "router1",
}


r1 = CiscoSSH(**device_params)
r1.send_show_command('sh ip int br')
