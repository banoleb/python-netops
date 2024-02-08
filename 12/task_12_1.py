from pprint import pprint
import sys
import subprocess
sys.path.append("..")



def ping_ip_addresses(ips):
    list_ok = []
    list_bad = []

    for ip in ips:
        result_ping = subprocess.run(
            ["ping", "-c", "2", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        if result_ping.returncode == 0:
            list_ok.append(ip)
        else:
            list_bad.append(ip)

    return list_ok, list_bad

pprint(ping_ip_addresses(["8.8.8.8","1.1.1.1","192.168.0.1"]))



