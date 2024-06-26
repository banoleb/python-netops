from sys import argv
import sqlite3

def get_data(select=None, params=None):
    connection = sqlite3.connect('dhcp_snooping.db')
    cursor = connection.cursor()
    if select==None and params==None:
        for row in cursor.execute('select * from dhcp'):
            print(row)
    else:
        for row in cursor.execute('select * from dhcp where '+select+' = '+params):
            print(row)   

list_a =["mac", "ip", "vlan", "interface", "switch"]
arggs= len(argv)
if arggs==1:
    get_data()
elif arggs==3:
    if argv[1] in list_a:
        get_data(argv[1], argv[2])
    else:
        print("Допустимые значения параметров: mac, ip, vlan, interface, switch")
else:
    print("Пожалуйста, введите два или ноль аргументов")
