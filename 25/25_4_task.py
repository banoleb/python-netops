from sys import argv
import sqlite3



def get_data(select=None, params=None):
    connection = sqlite3.connect('dhcp_snooping.db')
    cursor = connection.cursor()
    list_ok=[]
    list_down=[]
    if select==None and params==None:
        for row in cursor.execute('select * from dhcp'):
            if row[5]==1:
                list_ok.append(row)
            else:
                list_down.append(row)
    else:
        print("Информация об устройствах с такими параметрами", select, params)
        for row in cursor.execute('select * from dhcp where '+select+' = '+params):
            if row[5]==1:
                list_ok.append(row)
            else:
                list_down.append(row)

    print("Активные записи:")
    print(list_ok)
    print("Неактивные записи:")
    print(list_down)


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



