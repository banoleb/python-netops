import sqlite3
import os
import re
cwd = os.getcwd() 
import yaml
from tabulate import tabulate
# python3 parse_dhcp_snooping.py create_db
# python3 parse_dhcp_snooping.py add --db dhcp_snooping.db -h
# python3 parse_dhcp_snooping.py add --db dhcp_snooping.db sw1_dhcp_snooping.txt
# python3 parse_dhcp_snooping.py get -k vlan -v 76260
        

def add_data_to_db(connection, query, data):
    for row in data:
        try:
            with connection:
                connection.execute(query, row)
        except sqlite3.IntegrityError as err:
            print("При добавлении данных:", row, "Возникла ошибка:", err)

def create_db(dbfile, schema):
    if not os.path.exists(dbfile):
        conn = sqlite3.connect(dbfile)
        cursor = conn.cursor()
        with open(schema, 'r') as f:
            schema = f.read()
        cursor.executescript(schema)
    else:
        print("База данных существует")

def print_data_in_rows(data, active=True):
    data = list(data)
    if data:
        print(
            "\n{active} записи:\n".format(active="Активные" if active else "Неактивные")
        )
        print(tabulate(data))

def parse_dhcp_snoop(filenames):
    result_dict = []
    for count,items_files in enumerate(filenames):
        with open(cwd+"/new_data/"+items_files) as f:
            match = re.search('(\S+?)_\S+', items_files)
            if match != None:
                switch_name = match.group(1)
            regex =  r'^(\S+)\s+(\S+)\s+(\d+)\s+(\S+)\s+(\d+)\s+(\S+)$'
            for line in f:
                match = re.search(regex, line)
                if match:
                    mac_address = match.group(1)
                    ip_address = match.group(2)
                    vlan = match.group(3)
                    interface = match.group(6)
                    r_int = (mac_address,ip_address,vlan,interface,switch_name,1)
                    result_dict.append(r_int)
    return result_dict

def add_data_switches(dbfile, switchfile):
    print(dbfile,switchfile)
    query = "insert into switches values (?,?)"
    conn = sqlite3.connect(dbfile)
    with open(switchfile[0]) as f:
        ymlparse = yaml.safe_load(f)
    data = list(ymlparse["switches"].items())
    add_data_to_db(conn, query, data)
    conn.close()

def add_data(dbfile, data_files):
    conn = sqlite3.connect(dbfile)
    conn.execute("DELETE FROM dhcp WHERE last_active < datetime('now', '-7 days')")
    conn.execute("update dhcp set active = 0")
    query = "replace into dhcp values (?, ?, ?, ?, ?, ?,  datetime('now'))"
    result = parse_dhcp_snoop(data_files)
    add_data_to_db(conn, query, result)
    conn.commit()
    conn.close()

def get_data(dbfile, key, value):
    list_ok,list_down=[],[]
    list_a =["mac", "ip", "vlan", "interface", "switch"]
    conn = sqlite3.connect(dbfile)

    for row in conn.execute('select * from dhcp where '+key+' = '+value):
        if row[5]==1: list_ok.append(row)
        else: list_down.append(row)
    conn.close()
    printing(list_ok,list_down)

def get_all_data(dbfile):
    list_ok,list_down=[],[]
    conn = sqlite3.connect(dbfile)
    for row in conn.execute('select * from dhcp'):
        if row[5]==1: list_ok.append(row)
        else: list_down.append(row)
    conn.close()
    printing(list_ok,list_down)

def printing(data,data2):
    print("Активные записи:")
    print(tabulate(data))
    print("Неактивные записи:")
    print(tabulate(data2))