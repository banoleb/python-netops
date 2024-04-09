from netmiko.cisco.cisco_ios import CiscoIosSSH


class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

device_params = {
      
        "ip": "192.168.1.85",
        "username": "admin",
        "password": "cisco",
        "secret": "router1",
}


r1 = MyNetmiko(**device_params)
r1.send_command('sh ip int br')
