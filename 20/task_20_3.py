from jinja2 import Environment, FileSystemLoader
import yaml
from task_20_1 import generate_config

# так должен выглядеть вызов функции
if __name__ == "__main__":
    data_file = "data_files/ospf.yml"
    template_file = "templates/ospf.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))