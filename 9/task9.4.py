#!/usr/bin/env python3
from pprint import pprint
from sys import argv
import os

cwd = os.getcwd() 


#TASK9.4
ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status


def convert_config_to_dict(config_filename):

    with open(cwd+'/python/9/'+config_filename, 'r') as f:
        last_key=""
        result_dict={}
        temp_list=[]
        for line in f:
            if not line.startswith("!"):
                find =0
                check_f = ignore_command(line,ignore)
                if check_f == False:
                    if not line.startswith(" "):
                        result_dict[line.rstrip()]=""
                        last_key=str(line.rstrip())
                        temp_list.clear()  
                    else:
                        temp_list.append(line.rstrip())

                        result_dict[last_key]=temp_list.copy(); 
        del result_dict[""]
                        
        return result_dict
                    

pprint(convert_config_to_dict("config_sw1.txt"))