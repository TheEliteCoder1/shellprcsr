import os
import shutil
import colorama
import time
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

dir_path = os.path.dirname(os.path.realpath(__file__))

command_list = []
defenition_list = []

def add_command(c):
    return command_list.append(c)

def add_def(d):
    return defenition_list.append(d)

# adding commands to the command list

'''
System Types:
1. -a = about shell
2. -h = shell commands
3. --file -a = file specific commands
'''


# All True Type System Variables
ShellConfig = {"-a":"-a", "-h":"-h", "--file -a":"--file -a"}

# Commands List
add_command(f"{ShellConfig['-a']} commands")
add_command(f"{ShellConfig['-h']} txt [name] [folder]")
add_command(f"{ShellConfig['--file -a']} make [name] [extension] [folder]")
add_command(f"{ShellConfig['-h']} list files")
add_command(f"{ShellConfig['-h']} info")
add_command(f"{ShellConfig['--file -a']} move [file path] [new file path]")
add_command(f"{ShellConfig['-h']} quit shell -s")
add_command(f"{ShellConfig['-h']} make dir [name]")
add_command(f"{ShellConfig['--file -a']} del [path]")
add_command(f"{ShellConfig['-h']} del dir [path]")
add_command(f"{ShellConfig['-h']} cd dir [path]")
# functions to call
add_command("help()")

# adding defenitions to the defenitions list
add_def(f"{ShellConfig['-a']} commands: shows all commands")
add_def(f"{ShellConfig['-h']} txt [name] [folder]: creates a text file")
add_def(f"{ShellConfig['--file -a']} make [name] [extension] [folder]: creates any type of file")
add_def(f"{ShellConfig['-h']} list files: lists all of the files/directories from the current directory")
add_def(f"{ShellConfig['-h']} info: gives a brief description about the shell")
add_def(f"{ShellConfig['--file -a']} move [file path] [new file path]: moves an existing file to another directory")
add_def(f"{ShellConfig['-h']} quit shell -s: quits the shell")
add_def(f"{ShellConfig['-h']} make dir [name]: creates a new directory")
add_def(f"{ShellConfig['--file -a']} del [path]: deletes a file")
add_def(f"{ShellConfig['-h']} del dir [path]: deletes a folder")
add_def("help(): gives a description for each commands in the shell")
add_def(f"{ShellConfig['-h']} cd dir [path]: changes current directory to specified path")

'''
Shell User Properties
'''

user_list = ["default"]

def all_commands():
    for command in command_list:
        #Shows a list of all the commands, sorted by number(least to greatest).
        print(f"{command_list.index(command)}: {command}")

def make_text_file(folder, name):
    if os.path.exists(folder):
        file = open(f"{folder}/{name}.txt", "a")
        file.close()
    else:
        os.mkdir(folder)
        file = open(f"{folder}/{name}.txt", "a")
        file.close()

def make_file(folder, name, extension):
    if os.path.exists(folder):
        file = open(f"{folder}/{name}.{extension}", "a")
        file.close()
    else:
        os.mkdir(folder)
        file = open(f"{folder}/{name}.{extension}", "a")
        file.close()

def current_directories():
    for root, dirs, files in os.walk("."):
        for filename in files:
            print(Fore.CYAN + "  " + str(filename))
        for d in dirs:
            print(Fore.CYAN + "  " + str(d))

def make_dir(new):
    path = os.path.join(dir_path,new)
    os.mkdir(path)
    print(f"new directory '{new}' has been made.")

def info():
    Shell_Look = f"shell__{dir_path}>"
    print(f"This is a command line interface. '{Shell_Look}' is for multi-purpose use.")

def move_file(file_path, new_file_path):
    try:
        shutil.move(f"{file_path}", f"{new_file_path}")
        print(Fore.CYAN + "file has been moved successfully.")
    except:
        print(Fore.YELLOW + f"'{file_path}' is an invalid directory, and or the new file path is invalid.")
    
def del_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        time.sleep(0.1)
        print(Fore.CYAN + "file successfully deleted (execution in 0.1 seconds)")
    else:
        print(Fore.YELLOW + "This file path does not exist")

def del_folder(path):
    if os.path.exists(path):
        os.remove(path)
        time.sleep(0.1)
        print(Fore.CYAN + "folder successfully deleted (execution in 0.1 seconds)")
    else:
        print(Fore.YELLOW + "This folder path does not exist")
    

def call_help():
    for defenition in defenition_list:
        #Shows all defenitions for commands, sorted by number(least to greatest).
        print(f"{defenition_list.index(defenition)}: {defenition}")

def change_dir(path):
    if os.path.exists(path):
        os.getcwd(path)
    else:
        print(Fore.YELLOW + "This directory does not exist")
        
