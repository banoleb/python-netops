#!/usr/bin/env python3


#TASK7.1
result = {}

with open('/home/lvovivan/work/scripts_v3/python/ospf.txt', 'r') as f:
    for line in f:
        line_list = line.split()
        #print(line_list)
        arg1= line_list[1]
        arg2= line_list[2].replace("[", "").replace("]", "")
        arg4= line_list[4].replace(",", "")
        arg5= line_list[5].replace(",", "")
        arg6= line_list[6]

        message = ('Prefix "{0}" \n'
                'AD/Metric  "{1}" \n'
                'Next-Hop "{2}" \n'
                'Last update "{3}" \n'
                'Outbound Interface"{4}" \n')
        print(message.format(arg1,arg2,arg4,arg5,arg6))