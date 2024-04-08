from task_22_2a import CiscoTelnet

class CiscoTelnet_ex(CiscoTelnet):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.telnet.close()


tel_set = {
    "ip": "192.168.1.85",
    "username": "cisco",
    "password": "qwerty",
    "secret": "router1",
}

telneter = CiscoTelnet_ex(tel_set["ip"],tel_set["username"],tel_set["password"],tel_set["secret"])
print(telneter.send_show_command("sh ip int br"))