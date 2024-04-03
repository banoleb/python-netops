import time
import telnetlib

class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Password:")
        self._write_line(password)
        self._write_line("enable")
        self.telnet.read_until(b"Password:")
        self._write_line(secret)
        self._write_line("terminal length 0") 
        time.sleep(1)
        self.telnet.read_very_eager()

    def _write_line(self, line):
        self.telnet.write(line.encode("utf-8") + b"\n")

    def send_show_command(self, command):
        self._write_line(command)
        result = self.telnet.read_until(b"#").decode("utf-8")
        return result


tel_set = {
    "ip": "192.168.1.85",
    "username": "cisco",
    "password": "qwerty",
    "secret": "router1",
}
telneter = CiscoTelnet(tel_set["ip"],tel_set["password"],tel_set["secret"],tel_set["username"])
print(telneter.send_show_command("sh ip int br"))