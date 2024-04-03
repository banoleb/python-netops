class Network:
    all_allocated_ip = []

    def __init__(self, network):
        self.network = network
        self.hosts = tuple(
            str(ip) for ip in ipaddress.ip_network(network).hosts()
        )
        self.allocated = []

    def allocate(self, ip):
        if ip in self.hosts:
            if ip not in self.allocated:
                self.allocated.append(ip)
                type(self).all_allocated_ip.append(ip)
            else:
                raise ValueError(f"IP-адрес {ip} уже находится в allocated")
        else:
            raise ValueError(f"IP-адрес {ip} не входит в сеть {self.network}")