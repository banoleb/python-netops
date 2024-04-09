from base_connect_class import BaseSSH


class CiscoSSH(BaseSSH):
    def __init__(self, **device_params):
        if "device_type" not in device_params:
            get_inpute = input('Введите имя пользователя: ')
            device_params["device_type"]=get_inpute
        if "password" not in device_params:
            get_inpute = input('Введите пароль: ')
            device_params["device_type"]=get_inpute
        if "secret" not in device_params:
            get_inpute = input('Введите пароль для режима enable: ')
            device_params["device_type"]=get_inpute
        super().__init__(**device_params)
        self.ssh.enable()

device_params = {
      
        "ip": "192.168.1.85",
        "username": "admin",
        "password": "qwerty",
        "secret": "router1",
}


r1 = CiscoSSH(**device_params)
r1.send_show_command('sh ip int br')
