from concurrent.futures import ThreadPoolExecutor
from pprint import pprint
import yaml
import subprocess


def ping_ip_addresses(ips):
    list_ok = []
    list_bad = []
    result_ping = subprocess.run(
        ["ping", "-c", "2", ips],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if result_ping.returncode == 0:
        list_ok.append(ips)
    else:
        list_bad.append(ips)

    return list_ok, list_bad

with open('devices.yaml') as f:
    devices = yaml.safe_load(f)

with ThreadPoolExecutor(max_workers=3) as executor:
    future_list = []
    for device in devices:
        future = executor.submit(ping_ip_addresses, device['host'])
        print(device['host'])
        future_list.append(future)
    for f in future_list:
        print(f.result())