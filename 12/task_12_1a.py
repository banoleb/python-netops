from pprint import pprint
import ipaddress


list_ip=["10.1.1.1","10.1.1.1-10.1.1.10","10.1.1.1-10"]



def convert_ranges_to_ip_list(ip_addresses):
    ip_result = []
    for ip_address in ip_addresses:
        if "-" in ip_address:

            start_ip, stop_ip = ip_address.split("-")
            #print(start_ip, stop_ip)
            if "." not in stop_ip:
                #print(stop_ip)
                stop_ip = ".".join(start_ip.split(".")[:-1] + [stop_ip])
                #print(stop_ip)
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip = ipaddress.ip_address(stop_ip)
            for ip in range(int(start_ip), int(stop_ip)+1):
                #print(stop_ip+1)
                ip_result.append(str(ipaddress.ip_address(ip)))
        else:
            ip_result.append(ip_address)
    return ip_result

pprint(convert_ranges_to_ip_list(list_ip))
