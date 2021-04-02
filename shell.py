import colorama
import interpreter
from interpreter import *
from colorama import Fore, Back, Style
import time
import sys
import numpy as np
import cv2
import psutil
colorama.init(autoreset=True)

Shell_Look = f"#shellprcsr~"

def Shell():
    while True:
        shell = input(Shell_Look)
        
        if shell == "-h quit shell -s":
            print("Session ended...")
            sys.exit(0)
        if shell == "-a commands":
            all_commands()
        if shell == "-h txt":
            name = input("text file name: ")
            folder = input("folder: ")
            make_text_file(folder, name)
            print(f"text file made in: {folder}")
        if shell == "--file -a make":
            file_name = input("file name: ")
            file_extension = input("file extension: ")
            m_folder = input("folder: ")
            make_file(m_folder, file_name, file_extension)
            print(f".{file_extension} file made in: {m_folder}")
        if shell == "-h list files":
            print(f"Directory paths found in {dir_path}: ")
            current_directories()
        if shell == "-h info":
            info()
        if shell == "--file -a move":
            file_path = input("file path: ")
            new_file_path = input("new file path: ")
            move_file(file_path, new_file_path)
        if shell == "-h make dir":
            new = input("folder name: ")
            make_dir(new)
        if shell == "--file -a del":
            path_del = input("file path: ")
            del_file(path_del)
        if shell == "-h del dir":
            folder_path_del = input("folder path: ")
            del_folder(folder_path_del)
        if shell == "help()":
            call_help()
        if shell == "-h cd dir":
            new_path_dir = input("path: ")
            change_dir(new_path_dir)
        if shell == "-h camera":
            camera()
        if shell == "-h chk disk usg":
            path = "C:"
            stats = shutil.disk_usage(path)
            print(Fore.CYAN + f"Disk statistics: {stats}")
        if shell == "-h shout":
            sht = input("shout: ")
            print(sht)
        if shell == "-h virt memory prcs -s":
            print(psutil.virtual_memory())
        if shell == "--file -a write":
            uin = input("path to save doc: ")
            write_file(uin)
        if shell == "--file -a read":
            uint = input("path to file: ")
            read_file(uint)
        # Command Line Exception Handlers/Minimum Length Arguments
        '''
        for command in command_list:
            if shell != command and len(shell) > 0:
                print(Fore.RED + f"'{shell}', is not a valid command.")
                break
            elif shell == command and len(shell) > 0:
                continue
        '''


Shell()
