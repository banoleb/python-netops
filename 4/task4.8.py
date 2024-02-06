#!/usr/bin/env python3

#TASK48
ip = "10.1.1.1"
tmp_ip= ip.split(".")
ip_template = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(int(tmp_ip[0]), int(tmp_ip[1]), int(tmp_ip[2]), int(tmp_ip[3])))