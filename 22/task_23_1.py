class IPAddress:
    def __init__(self, ip):
        address, mask = ip.split("/")
        self._checking(address)
        self._checking_m(mask)
    def _checking(self,ip):
      
        ip_list = ip.split(".")
        for i in ip_list:
            if i.isdigit() and 0 <= int(i) <= 255 and len(ip_list) ==4:
                print(i)
            else:
                raise ValueError("Incorrect IPv4 address")
    def _checking_m(self,mask):
        if mask.isdigit() and 8 <= int(mask) <= 32:
            return True
        else:
            raise ValueError("Incorrect mask")


test = IPAddress('10.1.1.1/24')
