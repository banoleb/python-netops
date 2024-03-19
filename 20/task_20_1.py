from jinja2 import Environment, FileSystemLoader
import yaml
import re

def generate_config(template_file,data):

    regex = "(?P<dir>\S+)\/(?P<file>\S+)"
    regexsearch = re.search(regex, template_file)
    env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(regexsearch.group("file"))
    return template.render(data)


# так должен выглядеть вызов функции
if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file, data))