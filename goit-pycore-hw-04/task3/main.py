from colorama import Fore, Style
from pathlib import Path
import os, sys

def parse_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            print(f"{Fore.BLUE}\t{el}")
            parse_folder(el)
        else:
            print(f"{Fore.YELLOW}\t\t{el}")

def show_directory_structure(directory_path):
    p = Path(directory_path)
    if not p.exists() or not p.is_dir():
        print(f"{Fore.RED}Шлях {directory_path} не існує або не є директорією.")
        return print(Style.RESET_ALL)

    parse_folder(p)
    print(Style.RESET_ALL)

def show_usage():
    if os.name == "nt":
        print(f"{Fore.GREEN}Використання: python main.py C:\\шлях\\до\\директорії")
    else:
        print(f"{Fore.GREEN}Використання: python main.py /шлях/до/директорії")
    return print(Style.RESET_ALL)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        show_usage()
    else:
        directory_path = sys.argv[1]
        show_directory_structure(directory_path)
