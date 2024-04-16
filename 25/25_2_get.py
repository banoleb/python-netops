from sys import argv
import sqlite3

arg_1 = argv[1]
arg_2 = argv[2]


def get_data(select=None, params=None):
    connection = sqlite3.connect('dhcp_snooping.db')
    cursor = connection.cursor()
    if select==False and params==False:
        for row in cursor.execute('select * from dhcp'):
            print(row)
    else:
        for row in cursor.execute('select * from dhcp where '+select+' = '+params):
            print(row)   

list_a =["mac", "ip", "vlan", "interface", "switch"]
if arg_1 ==False:
    get_data()
elif arg_1 and arg_1 in list_a:
    get_data(arg_1, arg_2)
else:
    print("Пожалуйста, введите два или ноль аргументов")
    print("Допустимые значения параметров: mac, ip, vlan, interface, switch")
