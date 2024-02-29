import os
from pprint import pprint
from draw_network_graph import draw_topology
import csv
import datetime
cwd = os.getcwd() 




def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def convert_datetime_to_str(datetime_obj):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")


def write_last_log_to_csv(source_log,output):
    title=""
    temp= []
    with open(cwd+"/python/python_for_netops/17/"+source_log) as f:
        data = list(csv.reader(f))
        for count,i in enumerate(data):
            if count==0:
                title= i
                continue
            else:
                temp.append(i)
        list1 = temp.copy()
        for count,i in enumerate(temp):
            r1 = convert_str_to_datetime(i[2])
            for ii in temp:
                r2 = convert_str_to_datetime(ii[2])
                if (r1 < r2) and (i[1]==ii[1]):
                    list1.remove(i)
                    break 

    with open(output, "w") as dest:
        writer = csv.writer(dest)
        writer.writerow(title)
        for row in list1:
            writer.writerow(row)

if __name__ == "__main__":
    write_last_log_to_csv("mail_log.csv", "example_result.csv")






