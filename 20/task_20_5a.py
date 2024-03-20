from jinja2 import Environment, FileSystemLoader
from task_20_1 import generate_config

data = {
    "tun_num": 10,
    "wan_ip_1": "192.168.100.1",
    "wan_ip_2": "192.168.100.2",
    "tun_ip_1": "10.0.1.1 255.255.255.252",
    "tun_ip_2": "10.0.1.2 255.255.255.252",
}


def create_vpn_config(template1, template2, data_dict):
    config_1 = generate_config(template1, data_dict)
    config_2 = generate_config(template2, data_dict)
    return config_1, config_2



template_1 = "templates/gre_ipsec_vpn_1.txt"
template_2 = "templates/gre_ipsec_vpn_2.txt"
config_vpn1 = create_vpn_config(template_1, template_2, data)
config_vpn2 = create_vpn_config(template_1, template_2, data)
print(config_vpn1,config_vpn2)