import os
import platform
import subprocess
from datetime import date


def write_txt(table_str, config):
    func_output_path = os.getcwd() + config.output_path
    if not os.path.exists(func_output_path):
        os.mkdir(func_output_path)
    name = f"{config.output_name} from {config.target} on {date.today()}"
    increment = 1
    while os.path.exists(f"{func_output_path}{name} - {str(increment).zfill(3)}.txt"):
        increment = increment + 1
    with open(f'{func_output_path}{name} - {str(increment).zfill(3)}.txt', "w+") as write_file:
        write_file.write(table_str)


def write_clipboard(text):
    system = platform.system()

    if system == "Windows":
        process = subprocess.Popen(["clip"], stdin=subprocess.PIPE, shell=True)
        process.communicate(input=text.encode('utf-8'))
    elif system == "Darwin":
        process = subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE)
        process.communicate(input=text.encode('utf-8'))
    elif system == "Linux":
        try:
            process = subprocess.Popen(["xclip", "-selection", "clipboard"], stdin=subprocess.PIPE)
            process.communicate(input=text.encode('utf-8'))
        except FileNotFoundError:
            print("Fatal Error: xclip not found. Please install it using 'sudo apt-get install xclip' and try again.")
    else:
        raise Exception("Fatal Error: Unsupported OS")
