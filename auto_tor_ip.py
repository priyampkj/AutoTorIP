import os
import sys
import requests
import socks
import time


from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
os.system("clear")
cprint(figlet_format('AutoTorIP'),'green',attrs=['bold'])
print (chr(27)+"[34m"+"                                     Version : 3.0")
print
print (chr(27)+"[33m"+"Author : Rahat Khan Tusar(RKT)")
print (chr(27)+"[33m"+"Github : https://github.com/r3k4t")


def get_tor_ip():
    session = requests.session()

   
    session.proxies = {}
    session.proxies['http']='socks5://localhost:9050'
    session.proxies['https']='socks5://localhost:9050'

    try:
        r = session.get('http://httpbin.org/ip')
    except Exception as e:
        print  (e)
    else:
        return r.text

if __name__ == "__main__":
      while True:
        time.sleep(1)
        print (get_tor_ip())
        time.sleep(5)
        os.system("sudo service tor restart")
        
    
