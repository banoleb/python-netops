from task_21_4 import send_and_parse_show_command
from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
import os
import yaml


def send_and_parse_command_parallel(devices, command, templates_path, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = [
            executor.submit(send_and_parse_show_command, device, command, templates_path)
            for device in devices
        ]
        output = {device["host"]: f.result() for device, f in zip(devices, result)}
    return output



with open("devices.yaml") as f:
    devices = yaml.safe_load(f)
command = "sh ip int br"
templates_path = "templates"
pprint(send_and_parse_command_parallel(devices, command, templates_path))