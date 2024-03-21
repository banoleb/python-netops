from textfsm import clitable

def parse_command_dynamic(command_output, attributes_dict, index_file="index", templ_path="templates"):

    result = clitable.CliTable(index_file, templ_path)
    result.ParseCmd(command_output, attributes_dict)
    resultt=[]
    for i in result:
        resultt.append(dict(zip(result.header, i)))
    return resultt



if __name__ == "__main__":
    attributes = {"Command": "show ip int br", "Vendor": "cisco_ios"}
    with open("output/sh_ip_int_br.txt") as f:
        command_output = f.read()
    result = parse_command_dynamic(command_output, attributes)
    print(result)