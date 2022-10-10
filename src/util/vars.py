from os import environ
from dataclasses import dataclass
from colorama import Fore
from sys import platform

if platform == 'win32':
	DATAPATH = environ["PROGRAMFILES"] + "\\" + "CollectionApp"
elif platform == 'linux2':
	DATAPATH = '/usr/share'
else:
	print('This os is not supported at the moment.')

shellPadding = " " * 2
DashBoardDocumentation = """
-----------------------------------------------------------------
COLLECTION DASHBOARD
Commands:
	help: displays this message
	add: Create a new collection example -> add [name]
	delete: delete a particular collection example -> delete [index]
	edit: edit a collection using the index of the collection
	display: displays collections in this format: Index -> name
	Fdisplay: force display to display the paths
	key: display encryption key.

Notes:
	- Indexing will be provided
	- for the display command, if an index was provided, it loads and displays the content of a collection.
-----------------------------------------------------------------
"""

COLORS = {
	'black': Fore.BLACK ,
	'blue': Fore.BLUE,
	'cyan': Fore.CYAN,
	'green': Fore.GREEN ,
	'red': Fore.RED,
	'reset': Fore.RESET ,
	'white': Fore.WHITE ,
	'yellow': Fore.YELLOW,
	'lightblack': Fore.LIGHTBLACK_EX,
	'lightblue': Fore.LIGHTBLUE_EX,
	'lightcyan': Fore.LIGHTCYAN_EX,
	'lightgreen': Fore.LIGHTGREEN_EX,
	'lightmagenta': Fore.LIGHTMAGENTA_EX,
	'lightred': Fore.LIGHTRED_EX,
	'lightwhite': Fore.LIGHTWHITE_EX ,
	'lightyellow': Fore.LIGHTYELLOW_EX,
	'lightmagenta': Fore.MAGENTA
}
	
